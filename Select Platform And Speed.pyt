import arcpy

class Toolbox(object):


    def __init__(self):
        '''
        Toolbox constructor
        initiallize toolbox and list tools participating
        '''

        self.label = "Select Platform And Speed"
        self.alias = "SelectPlatformAndSpeed"
        self.tools = [SelectPlatformAndSpeed]

class SelectPlatformAndSpeed(object):
    '''
    '''

    def __init__(self):
        '''
        Tool constructor
        '''

        self.label = "Select Platform And Speed"
        self.description = "Select platform and speed fields from input table"

    def getParameterInfo(self):
        '''
        define parameters
        '''
        input_table = arcpy.Parameter(name='in_table',
                                         displayName='Input Table',
                                         direction='Input',
                                         datatype='GPTableView',
                                         parameterType='Required')

        input_platform_field = arcpy.Parameter(name='in_platform_field',
                                          displayName='Input Platform Field',
                                          direction='Input',
                                          datatype='Field',
                                          parameterType='Required')
        input_platform_field.parameterDependencies = [input_table.name]
        input_platform_field.filter.list = ["Text"]

        input_speed_field = arcpy.Parameter(name='in_speed_field',
                                          displayName='Input Speed Field',
                                          direction='Input',
                                          datatype='Field',
                                          parameterType='Required')
        input_speed_field.parameterDependencies = [input_table.name]
        input_speed_field.filter.list = ["DOUBLE","FLOAT","TEXT","LONG","SHORT"]

        input_speed_units = arcpy.Parameter(name='in_speed_units',
                                          displayName='Input Speed Units',
                                          direction='Input',
                                          datatype='GPString',
                                          parameterType='Required')
        speed_units = ["KPH", "MPH", "KNOTS"]
        input_speed_units.filter.list = speed_units
        input_speed_units.value = speed_units[0]

        out_platform_name = arcpy.Parameter(name='out_platform_name',
                                             displayName='Output Plaform Field Name',
                                             direction='Output',
                                             datatype='GPString',
                                             parameterType='Derived')

        out_speed_name = arcpy.Parameter(name='out_speed_name',
                                             displayName='Output Speed Field Name',
                                             direction='Output',
                                             datatype='GPString',
                                             parameterType='Derived')

        out_unit_type = arcpy.Parameter(name='out_unit_type',
                                             displayName='Output Speed Unit Type',
                                             direction='Output',
                                             datatype='GPString',
                                             parameterType='Derived')

        return[input_table,
               input_platform_field,
               input_speed_field,
               input_speed_units,
               out_platform_name,
               out_speed_name,
               out_unit_type,
               ]


    def execute(self, parameters, messages):

        # Get Plaform field name
        arcpy.SetParameter(4, parameters[1].valueAsText)
        # Get Speed field name
        arcpy.SetParameter(5, parameters[2].valueAsText)
        # Get Speed Units 
        arcpy.SetParameter(6, parameters[3].valueAsText)

        # arcpy.AddMessage(f"{parameters[1].valueAsText},
        #                    {parameters[2].valueAsText},
        #                    {parameters[3].valueAsText}")
