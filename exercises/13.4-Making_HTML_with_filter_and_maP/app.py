all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(colors):
    if colors["sexy"]==True:
        return colors["sexy"]

def generate_li(colorss):
    return "<li>"+colorss["label"]+"</li>"

filtered_list= list(filter(filter_colors, all_colors))
finished_list= list(map(generate_li, filtered_list))

print(finished_list)