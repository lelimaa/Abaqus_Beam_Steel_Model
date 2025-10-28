# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def ColumnMacro():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=145.105, 
        farPlane=232.019, width=328.868, height=213.205, cameraPosition=(
        7.50107, 0.649645, 188.562), cameraTarget=(7.50107, 0.649645, 0))
    s.resetView()
    s.resetView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=119.512, 
        farPlane=219.449, width=427.958, height=277.445, cameraPosition=(
        75.3878, -9.63978, 169.48), cameraTarget=(75.3878, -9.63978, 0.5))
    s.rectangle(point1=(100.0, 85.0), point2=(100.0, 100.0))
    s.rectangle(point1=(-100.0, 100.0), point2=(100.0, 85.0))
    s.rectangle(point1=(-100.0, -85.0), point2=(100.0, -100.0))
    s.rectangle(point1=(-5.0, 85.0), point2=(5.0, -85.0))
    s.CoincidentConstraint(entity1=v[8], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[10], entity2=g[9], addUndoState=False)
    s.FixedConstraint(entity=g[7])
    s.FixedConstraint(entity=g[5])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=158.163, 
        farPlane=180.798, width=85.6497, height=55.5266, cameraPosition=(
        8.33631, -71.9096, 169.48), cameraTarget=(8.33631, -71.9096, 0.5))
    s.autoTrimCurve(curve1=g[9], point1=(-0.832151412963867, -84.9060821533203))
    s.autoTrimCurve(curve1=g[11], point1=(-0.832151412963867, -85.2515029907227))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=162.496, 
        farPlane=176.465, width=52.8528, height=34.2644, cameraPosition=(
        5.7013, 80.1691, 169.48), cameraTarget=(5.7013, 80.1691, 0.5))
    s.autoTrimCurve(curve1=g[3], point1=(-1.10224342346191, 85.1515426635742))
    s.autoTrimCurve(curve1=g[13], point1=(-1.10224342346191, 84.9383926391602))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=151.595, 
        farPlane=187.366, width=135.353, height=87.7495, cameraPosition=(
        21.5851, -51.9176, 169.48), cameraTarget=(21.5851, -51.9176, 0.5))
    s.FilletByRadius(radius=10.0, curve1=g[10], nearPoint1=(-5.37553024291992, 
        -80.6443328857422), curve2=g[15], nearPoint2=(-8.67683410644531, 
        -85.0113372802734))
    s.FilletByRadius(radius=10.0, curve1=g[12], nearPoint1=(5.07859420776367, 
        -77.2326049804688), curve2=g[14], nearPoint2=(9.29692459106445, 
        -84.6019287109375))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=158.923, 
        farPlane=180.038, width=79.8974, height=51.7974, cameraPosition=(
        -1.17901, 88.0816, 169.48), cameraTarget=(-1.17901, 88.0816, 0.5))
    s.FilletByRadius(radius=10.0, curve1=g[16], nearPoint1=(-8.32430076599121, 
        85.1413192749023), curve2=g[10], nearPoint2=(-5.07644462585449, 
        82.3218688964844))
    s.FilletByRadius(radius=10.0, curve1=g[17], nearPoint1=(7.04890632629395, 
        84.8190994262695), curve2=g[12], nearPoint2=(4.99193000793457, 
        82.8051986694336))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=124.578, 
        farPlane=214.383, width=384.569, height=249.316, cameraPosition=(
        31.0074, -20.3431, 169.48), cameraTarget=(31.0074, -20.3431, 0.5))
    s.ObliqueDimension(vertex1=v[6], vertex2=v[7], textPoint=(126.98649597168, 
        -91.302978515625), value=15.0)
    s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(124.283645629883, 
        91.9073333740234), value=15.0)
    s.VerticalDimension(vertex1=v[3], vertex2=v[6], textPoint=(112.298416137695, 
        -93.4318237304688), value=200.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=115.419, 
        farPlane=223.542, width=463.011, height=300.17, cameraPosition=(24.342, 
        -20.483, 169.48), cameraTarget=(24.342, -20.483, 0.5))
    s.delete(objectList=(c[43], ))
    s.delete(objectList=(d[6], ))
    p = mdb.models['Model-1'].Part(name='Column', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Column']
    p.BaseSolidExtrude(sketch=s, depth=1500.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Column']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def BeamMacro():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=250.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=170.301, 
        farPlane=301.104, width=494.934, height=320.866, cameraPosition=(
        30.581, -13.4582, 235.702), cameraTarget=(30.581, -13.4582, 0))
    s1.Line(point1=(-60.0, 120.0), point2=(60.0, 120.0))
    s1.HorizontalConstraint(entity=g[2], addUndoState=False)
    s1.Line(point1=(-60.0, -120.0), point2=(60.0, -120.0))
    s1.HorizontalConstraint(entity=g[3], addUndoState=False)
    s1.Line(point1=(0.0, 120.0), point2=(0.0, -120.0))
    s1.VerticalConstraint(entity=g[4], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
    s1.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[4], 
        addUndoState=False)
    s1.CoincidentConstraint(entity1=v[5], entity2=g[3], addUndoState=False)
    s1.EqualDistanceConstraint(entity1=v[2], entity2=v[3], midpoint=v[5], 
        addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=465.238, height=301.614, 
        cameraPosition=(29.5751, -12.7546, 235.702), cameraTarget=(29.5751, 
        -12.7546, 0))
    p = mdb.models['Model-1'].Part(name='Beam', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Beam']
    p.BaseShellExtrude(sketch=s1, depth=500.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def EndPlateMacro():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=280.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=184.733, 
        farPlane=343.24, width=599.764, height=388.827, cameraPosition=(
        37.4099, 2.01034, 263.987), cameraTarget=(37.4099, 2.01034, 0))
    s.rectangle(point1=(-100.0, -140.0), point2=(100.0, 140.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=218.575, 
        farPlane=309.398, width=343.662, height=222.796, cameraPosition=(
        30.757, 54.4953, 263.987), cameraTarget=(30.757, 54.4953, 0))
    s.CircleByCenterPerimeter(center=(-50.0, 70.0), point1=(-35.0, 70.0))
    s.RadialDimension(curve=g[6], textPoint=(-53.9942474365234, 114.612037658691), 
        radius=9.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=201.602, 
        farPlane=326.371, width=472.104, height=306.065, cameraPosition=(
        65.7639, 0.536888, 263.987), cameraTarget=(65.7639, 0.536888, 0))
    s.linearPattern(geomList=(g[6], ), vertexList=(), number1=2, spacing1=100.0, 
        angle1=0.0, number2=2, spacing2=140.0, angle2=270.0)
    p = mdb.models['Model-1'].Part(name='End-Plate', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['End-Plate']
    p.BaseSolidExtrude(sketch=s, depth=10.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['End-Plate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def BoltMacro():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=24.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.6215, 
        farPlane=27.6333, width=42.8736, height=27.795, cameraPosition=(
        4.05581, -0.530763, 22.6274), cameraTarget=(4.05581, -0.530763, 0))
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(2.5, 3.0))
    s1.RadialDimension(curve=g[2], textPoint=(-7.04021072387695, 
        -0.898193717002869), radius=8.0)
    p = mdb.models['Model-1'].Part(name='Bolt', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Bolt']
    p.BaseSolidExtrude(sketch=s1, depth=25.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Bolt']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Bolt']
    f1, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f1[1], sketchUpEdge=e[0], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 
        25.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=67.35, gridSpacing=1.68, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Bolt']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=40.7486, 
        farPlane=74.5031, width=37.4892, height=24.3042, cameraPosition=(
        1.01909, 1.03923, 70.1259), cameraTarget=(1.01909, 1.03923, 25))
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(6.72, -8.4))
    s.RadialDimension(curve=g[3], textPoint=(-13.6616277694702, 7.25702571868896), 
        radius=12.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=39.5802, 
        farPlane=95.2975, width=58.1135, height=37.675, cameraPosition=(
        42.1507, 37.7195, 49.4373), cameraTarget=(3.21489, -1.21638, 10.5015))
    p = mdb.models['Model-1'].parts['Bolt']
    f, e1, d2 = p.faces, p.edges, p.datums
    p.SolidExtrude(sketchPlane=f[1], sketchUpEdge=e1[0], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s, depth=10.0, 
        flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=40.4684, 
        farPlane=96.4546, cameraPosition=(18.3727, 14.2253, -46.9084), 
        cameraUpVector=(-0.809309, 0.535631, 0.241078), cameraTarget=(0.919575, 
        1.10504, 16.8979))
    p = mdb.models['Model-1'].parts['Bolt']
    f1, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f1[4], sketchUpEdge=e[3], 
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0))
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=67.35, gridSpacing=1.68, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Bolt']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(-10.5, -5.46))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=39.4965, 
        farPlane=85.7553, width=48.2134, height=31.2567, cameraPosition=(
        1.80351, -0.588286, -45.1259), cameraTarget=(1.80351, -0.588286, 0))
    s1.RadialDimension(curve=g[3], textPoint=(-15.900857925415, 8.827805519104), 
        radius=12.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=37.7731, 
        farPlane=99.1499, width=74.4331, height=48.2549, cameraPosition=(
        21.6164, 18.7025, -45.1005), cameraTarget=(4.16331, 5.58223, 18.7058))
    p = mdb.models['Model-1'].parts['Bolt']
    f, e1, d2 = p.faces, p.edges, p.datums
    p.SolidExtrude(sketchPlane=f[4], sketchUpEdge=e1[3], sketchPlaneSide=SIDE1, 
        sketchOrientation=RIGHT, sketch=s1, depth=10.0, 
        flipExtrudeDirection=OFF)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(width=51.3491, height=33.2896, 
        cameraPosition=(18.6092, 14.1679, -46.8555), cameraTarget=(1.1561, 
        1.04767, 16.9508))
    p = mdb.models['Model-1'].parts['Bolt']
    s = p.features['Solid extrude-3'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Solid extrude-3'], filter=COPLANAR_EDGES)
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=39.3775, 
        farPlane=92.3247, cameraPosition=(23.6991, 59.9896, -0.915018), 
        cameraUpVector=(-0.944092, -0.0928975, -0.316322), cameraTarget=(
        0.859956, -1.61837, 14.2779))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=34.4345, 
        farPlane=97.2676, width=96.961, height=62.8598, cameraPosition=(
        18.3944, 63.2511, 4.33608), cameraTarget=(-4.44469, 1.64311, 19.529))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=27.3034, 
        farPlane=96.964, cameraPosition=(49.2168, 35.965, -1.65406), 
        cameraUpVector=(-0.821993, 0.532142, -0.202861), cameraTarget=(
        -5.18785, 2.30101, 19.6734))
    p = mdb.models['Model-1'].parts['Bolt']
    


