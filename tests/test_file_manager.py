from src.data_processors.file_manager import FileManager

def test_file_manager():
    file_name_input = "/home/mikhail/PycharmProjects/Gluing_Cards/tests/data/test.grd"
    file_manager = FileManager()
    (dem_in, region_bound_in, amount_x_in, amount_y_in) = file_manager.read(file_name_input)

    file_name_output = "/home/mikhail/PycharmProjects/Gluing_Cards/tests/data/test_out.grd"
    file_manager.write(file_name_output, dem_in, region_bound_in, amount_x_in, amount_y_in)

    (dem_out, region_bound_out, amount_x_out, amount_y_out) = file_manager.read(file_name_output)

    assert amount_x_out == amount_x_in
    assert amount_y_out == amount_y_in
    assert len(region_bound_out) == len(region_bound_in)

    for i in range(len(region_bound_out)):
        assert region_bound_out[i] == region_bound_in[i]

    for x in range(amount_x_in):
        for y in range(amount_y_in):
            assert dem_out[x][y] == dem_in[x][y]

