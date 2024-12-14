import arcpy
import arcpy.mapping
arcpy.env.workspace=r'C:\Buffer_analysis\input'
arcpy.env.overwriteOutput=True
shape_data=arcpy.ListFeatureClasses()
print (shape_data)
point_data=r'C:\Buffer_analysis\input\buildings.shp'

buffer_distance="1000 Meters"
road=r"C:\Buffer_analysis\input\roads.shp"
buffer_output=r"C:\Buffer_analysis\output\point_buffer\point_out.shp"

arcpy.Buffer_analysis(point_data,buffer_output,buffer_distance,dissolve_option='ALL')
print ("Buffer analysis Successful")
pdf_output=r'C:\Buffer_analysis\output\buffermapOutput\pointmap.pdf'

mxd_path=r"C:\Buffer_analysis\map\blankmap.mxd"

intersect_out=r"C:\Buffer_analysis\output\intersection\intersect_out.shp"

arcpy.Intersect_analysis([buffer_output,road],intersect_out)
print ("Intersection analysis Successful")

mxd=arcpy.mapping.MapDocument(mxd_path)

df=arcpy.mapping.ListDataFrames(mxd)[0]
buffer_layar=arcpy.mapping.Layer(buffer_output)
interaction_layar=arcpy.mapping.Layer(intersect_out)

arcpy.mapping.AddLayer(df,buffer_layar,add_position="TOP")
arcpy.mapping.AddLayer(df,interaction_layar,add_position='TOP')
arcpy.mapping.ExportToPDF(mxd,pdf_output)
