import os
import unittest
import subprocess
import random
try: # Try to import the local version first (usually works when executed from the command line with Python directly)
    import SparseDenseEvaluation as SparseDense
except ImportError: # Only works when you execute it with the '-m unittest' parameter from stonne/stonne directory
    import tests.TileGenerator.MyGenerator.SparseDenseEvaluation as SparseDense


PERFORMANCE_TOLERANCE = 0.2
GENERATOR = "MyGenerator"


class TestSparseDenseRealModels(unittest.TestCase):
    """
    Test cases to test the generation of MyGenerator for SparseDense layers.
    It uses real model layers from Alexnet, MobileNet, ResNet-50 and VGG-16.
    For each test, it runs a simulation of the layer generating the tile with MyGenerator.
    Later, it searches for the best possible tile for this layer.
    At last, it compares the generated tile results with the best possible tile results,
    passing the test only if the speedup fits in the tolerance margin.
    Note: accumulation_buffer is always 1
    """

    # TODO: should we consider greater batch sizes than 1?

    @classmethod
    def setUpClass(cls):
        # builds the STONNE executable
        proc = subprocess.Popen(["make", "all"])
        proc.wait()

    def testSparseDenseFc1Alexnet(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=4096, N=1, K=9216, sparsity=97, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    def testSparseDenseFc2Alexnet(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=4096, N=1, K=4096, sparsity=91, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    def testSparseDenseFc3Alexnet(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=1000, N=1, K=4096, sparsity=90, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    def testSparseDenseFc1MobileNet(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=1000, N=1, K=1024, sparsity=75, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    def testSparseDenseFc1ResNet(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=1000, N=1, K=2048, sparsity=89, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    def testSparseDenseFc1VGG16(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=4096, N=1, K=25088, sparsity=93, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    # Same mapping of Fc2Alexnet, different sparsity
    def testSparseDenseFc2VGG16(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=4096, N=1, K=4096, sparsity=93, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))

    # Same mapping of Fc3Alexnet, different sparsity
    def testSparseDenseFc3VGG16(self):
        results = []
        for num_ms in [128, 256, 512]:
            results.append(SparseDense.evaluate(num_ms=num_ms, dn_bw=num_ms, rn_bw=num_ms, M=1000, N=1, K=4096, sparsity=93, tolerance=PERFORMANCE_TOLERANCE, generator=GENERATOR))
        self.assertTrue(all(results))


# Main method to execute all testcases of MyGenerator for SparseDense/FC layers
if __name__ == "__main__":
    if not os.getcwd().endswith('stonne/stonne'):
        print("Please run this SparseDense.evaluate script from the stonne/stonne directory")
        exit(1)

    unittest.main()
