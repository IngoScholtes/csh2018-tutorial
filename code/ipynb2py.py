#%%
import json

def remove_code(ipynb_file, output_file):
    print('Removing code from ipynb file ...')   
    with open(ipynb_file, 'r') as f:
        notebook = json.load(f)
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':               
               cell['source'] = []
               cell['outputs'] = []
    with open(output_file, 'w') as f:
        json.dump(notebook, f)  
    print('Done.')

def extract_code(ipynb_file, output_file=None):
    """
    Converts an ipython notebook file to a plain .py file that 
    only contains the code cells. Nice to use as a template for 
    generating the live solution.

    Parameters:
    -----------
    ipynb_file: str
        filename of ipynb jupyter notebook file
    output_file: str
        where to store the .py output file
    blank_code: bool
        if True, this will generate blank code cells, resulting in 
        files that can be used as exercise skeletons. If False (default), 
        all code cells will be populated with actual code.
    todo_msg: str
        A string text by which code cells will be replaced if blank_code 
        is set to True. If set to None, no todo message will be created.
    """
    print('Converting ipynb file ...')
    output = ''
    with open(ipynb_file, 'r') as f:
        notebook = json.load(f)
        for cell in notebook['cells']:
           if cell['cell_type'] == 'code':
                cell_output = '#%% In [' + str(cell['execution_count']) + ']\n'
                for line in cell['source']:
                    # remap relative path data directory from jupyter notebook to VS Code                
                    cell_output += line.replace('../', '')                
                cell_output += '\n\n'
                output += cell_output
    with open(output_file, 'w') as f:
        f.write(output)    
    print('Done.')

def convert(ipynb_file, output_file=None, blank_code = False, todo_msg = '# TODO: Fill code here'):
    """
    Converts an ipython notebook file to a plain .py file that 
    can be used with the jupyter extension in Visual Studio Code. 
    Markdown cells in the notebook will be output properly formatted 
    in the VS Code Results panel.

    Parameters:
    -----------
    ipynb_file: str
        filename of ipynb jupyter notebook file
    output_file: str
        where to store the .py output file
    blank_code: bool
        if True, this will generate blank code cells, resulting in 
        files that can be used as exercise skeletons. If False (default), 
        all code cells will be populated with actual code.
    todo_msg: str
        A string text by which code cells will be replaced if blank_code 
        is set to True. If set to None, no todo message will be created.
    """
    print('Converting ipynb file {} to {} ...'.format(ipynb_file, output_file))
    output = '#%%\nimport markdown\n' \
             'from IPython.core.display import display, HTML\n'\
             'def md(str):\n'\
             '    display(HTML(markdown.markdown(str + "<br />")))\n\n'
    with open(ipynb_file, 'r') as f:
        notebook = json.load(f)
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                cell_output = '#%%\nmd("""\n'
                for line in cell['source']:
                    cell_output += line                    
                cell_output += '\n""")\n\n'
                output += cell_output
            elif cell['cell_type'] == 'code':
                cell_output = '#%% In [' + str(cell['execution_count']) + ']\n'
                if not blank_code or cell['source'][0].startswith('%NOREMOVE'):
                    for line in cell['source']:
                        # remap relative path data directory from jupyter notebook to VS Code                
                        cell_output += line.replace('../', '').replace('from state_lumping_network', 'from solutions.state_lumping_network')
                elif todo_msg is not None:
                    cell_output += todo_msg + '\n'
                cell_output += '\n\n'
                output += cell_output
    with open(output_file, 'w') as f:
        f.write(output)    
    print('Done.')


# To apply the script to the sample solutions, just execute the following cells:
#%% Unit 2
#convert('code/2_pathpy.ipynb', 'code/2_pathpy_.py', blank_code=True, todo_msg=None)
extract_code('code/2_pathpy.ipynb', 'code/2_pathpy_code.py')
#remove_code('solutions/2_pathpy.ipynb', 'code/2_pathpy.ipynb')
convert('code/2_pathpy.ipynb', 'code/2_pathpy.py', blank_code=False, todo_msg=None)

#%% Unit 3
#convert('solutions/3_higher_order.ipynb', 'code/3_higher_order.py', blank_code=True, todo_msg=None)
extract_code('code/3_higher_order.ipynb', 'code/3_higher_order_code.py')
#remove_code('solutions/3_higher_order.ipynb', 'code/3_higher_order.ipynb')
convert('code/3_higher_order.ipynb', 'code/3_higher_order.py', blank_code=False, todo_msg=None)

#%% Unit 4
#convert('solutions/4_temporal_networks.ipynb', 'code/4_temporal_networks.py', blank_code=True, todo_msg=None)
extract_code('code/4_temporal_networks.ipynb', 'code/4_temporal_networks_code.py')
#remove_code('solutions/4_temporal_networks.ipynb', 'code/4_temporal_networks.ipynb')
convert('code/4_temporal_networks.ipynb', 'code/4_temporal_networks.py', blank_code=False, todo_msg=None)

#%% Unit 5
extract_code('code/5_exploration.ipynb', 'code/5_exploration_code.py')
convert('code/5_exploration.ipynb', 'code/5_exploration.py', blank_code=False, todo_msg=None)


#%% Unit 6
#convert('solutions/6_multi_order.ipynb', 'code/6_multi_order.py', blank_code=True, todo_msg=None)
extract_code('code/6_multi_order.ipynb', 'code/6_multi_order_code.py')
#remove_code('solutions/6_multi_order.ipynb', 'code/6_multi_order.ipynb')
convert('code/6_multi_order.ipynb', 'code/6_multi_order.py', blank_code=False, todo_msg=None)

#%% Unit 7
#convert('solutions/7_optimal_analysis.ipynb', 'code/7_optimal_analysis.py', blank_code=True, todo_msg=None)
extract_code('code/7_optimal_analysis.ipynb', 'code/7_optimal_analysis_code.py')
#remove_code('solutions/7_optimal_analysis.ipynb', 'code/7_optimal_analysis.ipynb')
convert('code/7_optimal_analysis.ipynb', 'code/7_optimal_analysis.py', blank_code=False, todo_msg=None)

#%% Unit 8
convert('code/8_exploration.ipynb', 'code/8_exploration.py', blank_code=False, todo_msg=None)
extract_code('code/8_exploration.ipynb', 'code/8_exploration_code.py')
