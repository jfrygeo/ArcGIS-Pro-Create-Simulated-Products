import arcpy
import os, sys

class Toolbox(object):


    def __init__(self):
        '''
        Toolbox constructor
        initiallize toolbox and list tools participating
        '''

        self.label = "Table to Table"
        self.alias = "TableToTable"
        self.tools = [TableToTable]

class TableToTable(object):
    '''
    '''

    def __init__(self):
        '''
        Tool constructor
        '''

        self.label = "Table to Table"
        self.description = "Automated way to update the field mapping in Table to Table gp tool"

    def getParameterInfo(self):
        '''
        define parameters
        '''
        in_rows = arcpy.Parameter(name='in_rows',
                                         displayName='In Rows',
                                         direction='Input',
                                         datatype='GPTableView',
                                         parameterType='Required')

        out_path = arcpy.Parameter(name='out_path',
                                          displayName='Out Path',
                                          direction='Input',
                                          datatype='DEFolder',
                                          parameterType='Required')
        out_name = arcpy.Parameter(name='out_name',
                                          displayName='Out Name CSV',
                                          direction='Input',
                                          datatype='GPString',
                                          parameterType='Required')
        out_name.values = '.csv'

        output_table = arcpy.Parameter(name='output_table',
                                             displayName='Output Table',
                                             direction='Output',
                                             datatype='GPTableView',
                                             parameterType='Derived')
                                    

        return[in_rows,
               out_path,
               out_name,
               output_table,
               ]


    def execute(self, parameters, messages):
        #in_rows = arcpy.GetParameterAsText(0)
        #out_path = arcpy.GetParameterAsText(1)
        #out_name = arcpy.GetParameterAsText(2)
        
        
        #fieldmappings = arcpy.FieldMappings()
        #newmapping = fieldmappings.addTable(parameters[0].valueAsText)
       

 
        #Run the TableToTable tool
        arcpy.TableToTable_conversion(in_rows=parameters[0].valueAsText, out_path=parameters[1].valueAsText, out_name=parameters[2].valueAsText, where_clause=None, field_mapping=None, config_keyword=None)
        arcpy.SetParameter(3, os.path.join(parameters[1].valueAsText,parameters[2].valueAsText))
        #arcpy.FieldMappings.removeAll(newmapping)
