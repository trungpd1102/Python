import os
# current_directory = os.path.dirname(os.path.abspath(__file__))
# # print(f'current_directory: {current_directory}')
# data_path = os.path.join(current_directory, '..')
# # print(f'data_path: {data_path}')

# # read data from HTML file
# with open(os.path.join(data_path, "2021-03-20_pyldavis.html"), "r") as data:
#     htmlLink = str(data.read())

# print(htmlLink)


def test_return():
	return {"a": "aaaa",
			 "b": "bbbbb"
			}
data = test_return()
print(data["a"])


# print(__file__)
# print(os.path.join(os.path.dirname(__file__), '..'))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.abspath(os.path.dirname(__file__)))


