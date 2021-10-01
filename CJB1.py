from numpy import array
from pybimstab.slope import NaturalSlope
from pybimstab.bim import BlocksInMatrix
from pybimstab.slipsurface import CircularSurface, TortuousSurface
from pybimstab.slices import MaterialParameters, Slices
from pybimstab.slopestabl import SlopeStabl
terrainCoords = array([[-10, -9.06, -3.08, -1.97, 0.04, 0.98, 8.03, 9.02, 10],
                       [14.96,  14.05, 12.08, 12.03, 9.07, 5.03, 4.94, 1.98, 0]])
slope = NaturalSlope(terrainCoords)
bim = BlocksInMatrix(slopeCoords=slope.coords, blockProp=0.15,
                     tileSize=0.7, seed=100)
preferredPath = CircularSurface(
    slopeCoords=slope.coords, dist1=2, dist2=10, radius=35)
surface = TortuousSurface(
    bim, dist1=7.5, dist2=11.5, heuristic='euclidean',
    reverseLeft=False, reverseUp=False, smoothFactor=2,
    preferredPath=preferredPath.coords, prefPathFact=2)
material = MaterialParameters(
    cohesion=1.48, frictAngle=58.23, unitWeight=11.85,
    blocksUnitWeight=None, wtUnitWeight=9.8)
slices = Slices(
    material=material, slipSurfCoords=surface.coords,
    slopeCoords=slope.coords, numSlices=10, bim=bim)
stabAnalysis = SlopeStabl(slices, seedFS=1, Kh=0)
fig = stabAnalysis.plot()
