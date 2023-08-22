import random
from init import init

input_filename = 'in/out/input.txt'
output_filename = 'in/out/vpc.tf'


with open(input_filename, 'r') as f:
    content = f.read()

chunks = content.split('resource')

matching_chunks = []
for chunk in chunks:
    if 'Name =' in chunk:
        if 'resourceOverriding' in chunk or 'Overriding' in chunk or 'number of parameters' in chunk or \
           'Loading meta from' in chunk or 'from output file' in chunk:
            continue
        
    
        start_idx = chunk.find('tags = {')
        if start_idx != -1:
            end_idx = chunk.find('}', start_idx)
            if end_idx != -1:
                tags_block = chunk[start_idx:end_idx + 1]
                resource_lines = 'resource' + chunk.split('tags =')[0]  
                matching_chunks.append(resource_lines + '\n    ' + tags_block + '\n  }' ) 


if matching_chunks:
    random_chunk = random.choice(matching_chunks)


    with open(output_filename, 'w') as f:
        f.write(random_chunk)


init()