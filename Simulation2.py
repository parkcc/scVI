from scvi.harmonization.utils_chenling import CompareModels

use_cuda = True
import numpy as np
from scipy.sparse import csr_matrix

from scvi.dataset.dataset import GeneExpressionDataset


import sys
models = str(sys.argv[1])
plotname = 'Sim2'

countUMI = np.load('../sim_data/count.UMI.npy')
countnonUMI = np.load('../sim_data/count.nonUMI.npy')
labelUMI = np.load('../sim_data/label.UMI.npy').astype('int')
labelnonUMI = np.load('../sim_data/label.nonUMI.npy').astype('int')

dataset1 = GeneExpressionDataset(
            *GeneExpressionDataset.get_attributes_from_matrix(
                csr_matrix(countUMI.T), labels=labelUMI.astype('int')),
            gene_names=['gene'+str(i) for i in range(2000)], cell_types=['type'+str(i+1) for i in range(5)])

dataset2 = GeneExpressionDataset(
            *GeneExpressionDataset.get_attributes_from_matrix(
                csr_matrix(countnonUMI.T), labels=labelnonUMI.astype('int')),
            gene_names=['gene'+str(i) for i in range(2000)], cell_types=['type'+str(i+1) for i in range(5)])

dataset1.subsample_genes(dataset1.nb_genes)
dataset2.subsample_genes(dataset2.nb_genes)

gene_dataset = GeneExpressionDataset.concat_datasets(dataset1, dataset2)
gene_dataset.subsample_genes(gene_dataset.nb_genes)
# CompareModels(gene_dataset, dataset1, dataset2, plotname, 'writedata')

CompareModels(gene_dataset, dataset1, dataset2, plotname, models)