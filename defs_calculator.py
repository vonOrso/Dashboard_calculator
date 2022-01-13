from PIL import Image, ImageDraw, ImageFont
import copy

def size_calcs(size_array, size_int, border_size = 8):
    n_elements = len(size_array)
    n_auto_elements = size_array.count('Auto')
    if n_auto_elements != 0:
        sum_non_auto = sum([i for i in size_array if not isinstance(i, str)])
        auto_vert = (size_int - border_size * (n_elements + 1) - sum_non_auto) / n_auto_elements
    else:
        auto_vert = 0
    return float(auto_vert), n_elements

def replase_apply(array_for_replace, value):
    return [float(i) if i !='Auto' else value for i in array_for_replace]

# Main function
def dashboard_calculator(db_width: int, 
                         db_height: int, 
                         db_hor_sizes, 
                         db_ver_sizes,
                         global_borders:int = 8,
                         img_name_and_format: str = '',
                         save: str = 'No',
                         show: str = 'Yes',
                         font = ImageFont.truetype("arial.ttf", size=30), 
                         background_color: str = '#E5E5E5', 
                         block_color: str = 'white', 
                         text_color: str = '#484848',
                         outer_padding: int = 4, 
                         text_pos_correction: int = 35):
    
#     Changing the format to float is necessary for a uniform display of numbers
    global_borders = float(global_borders)
#     Making copies to avoid problems
    db_x_pos = copy.deepcopy(db_hor_sizes)
    db_y_pos = copy.deepcopy(db_ver_sizes)
    db_hor_sizes_calc = copy.deepcopy(db_hor_sizes)
    db_ver_sizes_calc = copy.deepcopy(db_ver_sizes)
#     Calculation of automatic dimensions
    ver_auto_size, n_hor_lines = size_calcs(db_ver_sizes_calc, db_height)
    db_ver_sizes_calc = replase_apply(db_ver_sizes_calc, ver_auto_size)
#     Starting positions
    start_x = global_borders
    start_y = global_borders
    add_modifier_y = 0
#     Creating an empty picture
    img = Image.new('RGB', (db_width, db_height), background_color)
    idraw = ImageDraw.Draw(img)

    for i in range(n_hor_lines):
        db_y_pos[i] = global_borders * (i + 1) + add_modifier_y
        add_modifier_y += db_ver_sizes_calc[i]

        temp_add_modifier = 0
        temp_auto_size, temp_n_lines = size_calcs(db_hor_sizes_calc[i], db_width)
        db_hor_sizes_calc[i] = replase_apply(db_hor_sizes_calc[i], temp_auto_size)
        for j in range(temp_n_lines):
            db_x_pos[i][j] = global_borders * (j + 1) + temp_add_modifier
            temp_add_modifier += db_hor_sizes_calc[i][j]
#             Creating a block
            idraw.rectangle((db_x_pos[i][j], 
                             db_y_pos[i], 
                             db_x_pos[i][j] + db_hor_sizes_calc[i][j] - 1, 
                             db_y_pos[i] + db_ver_sizes_calc[i] - 1), fill = block_color)
#             Creating a label with x and y
            idraw.text((db_x_pos[i][j] + outer_padding, db_y_pos[i] + outer_padding), 
                       'x: %s; y: %s' % (db_x_pos[i][j], db_y_pos[i]),
                       fill= text_color, font=font)
#             Creating a label with w and h
            idraw.text((db_x_pos[i][j] + outer_padding, db_y_pos[i] + text_pos_correction), 
                       'w: %s; h: %s' % (db_hor_sizes_calc[i][j], db_ver_sizes_calc[i]),
                       fill= text_color, font=font)

    if show == 'Yes':
        img.show()
        
    if save == 'Yes':
        img.save(img_name_and_format)
    
    return 'Completed'