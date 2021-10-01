from numpy import array
from pybimstab.slope import NaturalSlope
from pybimstab.bim import BlocksInMatrix
from pybimstab.slipsurface import CircularSurface, TortuousSurface
from pybimstab.slices import MaterialParameters, Slices
from pybimstab.slopestabl import SlopeStabl
terrainCoords = array([[-4.8958, -4.5313, -4.0365, -2.0313, -1.0156, 0.026042, 0.96354, 1.9792, 2.0313,
                        8.0469, 9.0625, 10.026],
                       [10.026, 9.5325, 9.013, 8.0519, 8.0519, 7.0649,
                        5.064935, 5.038961, 4.05195, 4, 3.013, 0]])
slope = NaturalSlope(terrainCoords)
bim = BlocksInMatrix(slopeCoords=slope.coords, blockProp=0.15,
                     tileSize=0.8, seed=1)
preferredPath = CircularSurface(
    slopeCoords=slope.coords, dist1=1, dist2=10, radius=20)
surface = TortuousSurface(
    bim, dist1=8.665, dist2=9.665, heuristic='euclidean',
    reverseLeft=False, reverseUp=False, smoothFactor=2,
    preferredPath=preferredPath.coords, prefPathFact=2)
material = MaterialParameters(
    cohesion=2.24, frictAngle=44.29, unitWeight=12.20,
    blocksUnitWeight=None, wtUnitWeight=9.8)
slices = Slices(
    material=material, slipSurfCoords=surface.coords,
    slopeCoords=slope.coords, numSlices=10, bim=bim)
stabAnalysis = SlopeStabl(slices, seedFS=1, Kh=0)
fig = stabAnalysis.plot()
