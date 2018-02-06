import pyexcel

a_list_of_dictionaries = [
    {
    'title':'SU 25',
    'link': 'http://google.com'
    },
    {
    'title':'SU 25',
    'link': 'http://google-2.com'
    },
    {'title':'SU 25',
    'link': 'http://google-3.com'
    }
]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="Ngoc_phuc.xls")
