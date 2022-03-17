from extract_data import get_invoice_data
from data import data_page_1, data_page_2
from updateGSheet import updateGsheet

if __name__ == '__main__':

    img_paths = ['Images\Yusen_2_invoices_1.png', 'Images\Yusen_2_invoices_2.png']
    data_to_send = [data_page_1, data_page_2]
    
    if len(img_paths) != len(data_to_send):
        exit(0)
    
    new_row = []
    for index in range(len(img_paths)):
        extracted_data = get_invoice_data(img_paths[index], data_to_send[index])
        new_row +=list(extracted_data.values())

    # updateGsheet(file_name, sheet_name)  
    print('------ Done -------')