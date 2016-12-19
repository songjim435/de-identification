import os

from common.base import *
from dptable.variance_reduce import VarianceReduce
from dptable.inference import Inference
from prob_models.jtree import JunctionTree
from spark_exp.data_dist import DataDist
from spark_exp.dep_graph_dist import DepGraphDist
from spark_exp.histogramdd_dist import HistogramddDist
from spark_exp.simulate_dist import SimulateDist

from time import time

class DPTableDist(Base):
	def __init__(self, data, eps1=10, eps2=0.2, partitions_num = 120):
		self.eps1 = eps1
		self.eps2 = eps2
		self.LOG = Base.get_logger("DPTableDist")
		# read data
		self.data = data
		# repartition
		self.data.coalesce(partitions_num)
		self.df = data.get_df()
		self.domains = data.get_domains()

	def run(self):
		# build markov graph
		graph = DepGraphDist(self.data, eps1 = self.eps1)
		edges = graph.fit()
		nodes = self.domains.keys()
		
		# build junction tree
		jtree_path = c.TEST_JTREE_FILE_PATH
		jtree = JunctionTree(edges, nodes, jtree_path)
		
		# merge cliques to reduce variance
		jtree_cliques = jtree.get_jtree()['cliques']
		var_reduce = VarianceReduce(self.domains, jtree_cliques, 0.2)
		opted_marginals = [sorted(marginal) for marginal in var_reduce.main()]
		
		# find histograms
		combined_queries = self.combine_cliques_for_query(jtree_cliques, opted_marginals)
		hist_dist = HistogramddDist(self.data)
		histogramdds = hist_dist.histogram_dist(combined_queries)
		
		# do inference
		inference = Inference(
			self.data, 
			jtree_path,
			self.domains, 
			opted_marginals,
			histogramdds,
			self.eps2)
		model = inference.execute()
		
		# sampling
		simulator = SimulateDist(model, self.data.get_nrows())
		df = simulator.run()
		
		t = time()
		save_path = os.path.join('/data/synthetic', 'sim_%d' % t)
		self.LOG.info('Writing data to path %s.' % save_path)
		df.write.parquet(save_path)
		self.LOG.info('Writing data complete in %d secs.' % (time() - t))
