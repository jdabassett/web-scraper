from playwright.sync_api import sync_playwright
import sys
from datetime import datetime


def get_citations_needed_count(str_par_url: str) -> int:
    """
    Will scrape wikipedia webpage for number of missing citations.
    :param str_par_url: str
    :return: list
    """
    with sync_playwright() as p:
        obj_browser = p.chromium.launch()
        obj_page = obj_browser.new_page()
        try:
            obj_page.goto(str_par_url)
            int_count = obj_page.get_by_title('Wikipedia:Citation needed').count()
        except Exception:
            raise ValueError("Unable to open url provided.")
        obj_browser.close()
        return int_count


def get_citations_needed_report(str_par_url: str) -> list:
    """
    Will scrape wikipedia webpage for missing citations and return a list of paragraphs.
    :param str_par_url: str
    :return: list
    """
    with sync_playwright() as p:
        obj_browser = p.chromium.launch()
        obj_page = obj_browser.new_page()
        obj_page.goto(str_par_url)
        obj_children = obj_page.get_by_title('Wikipedia:Citation needed')
        list_nearest_parents = obj_page.get_by_role("paragraph").filter(has=obj_children).all_inner_texts()
    return list_nearest_parents


if __name__ == "__main__":

    # assign url and filename variables
    str_url = str(sys.argv[2])
    str_report_name = str(sys.argv[1])
    if any(True if char in '\ /:*?"<>|' else False for char in str_report_name):
        raise ValueError("Must supply file name that doesn't contain these characters.(/:*?\"<>|')")

    # retrieve number of lacking citations and report
    list_citation_needed = get_citations_needed_report(str_url)
    int_citation_needed = get_citations_needed_count(str_url)

    # save and append to file
    with open(f'{str_report_name}_report.txt', "a") as file:
        file.write("\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        file.write(f"Website: {str_url}\n")
        file.write(f"Number of 'Citation needed' in given website: {int_citation_needed}\n")
        file.writelines(f"{i+1}: {string}\n" for i, string in enumerate(list_citation_needed))

    # print to console
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    print(f"Website: {str_url}\n")
    print("Number of 'Citation needed' in given website:", int_citation_needed)
    print('Report of paragraphs from website that need citation:')
    for i in list_citation_needed:
        print(i)
        print("")
