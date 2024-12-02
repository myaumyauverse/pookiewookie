final_response = requests.get(final_link)
#             final_soup = BeautifulSoup(final_response.content, 'html.parser')
            
#             # Extract the text content from the final link URL
#             final_content = final_soup.find("main", id="content")
#             if final_content:
#                 print(final_content.get_text())
#             else:
#                 print("Content not found in:", final_link)
# else:
#     print('Error: Sidebar content not found.')
# # Make a request to the website
# url = 'https://axios-http.com/docs/intro'  # Replace with the URL of the website you want to extract content from
# response = requests.get(url)

# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Extract the main content
# main_content = soup.find('div', class_='main')  # Replace with the specific class or tag of the main content

# # Print the main content
# if main_content is not None:
#     print(main_content.get_text())
# else:
#     print('Main content not found on the page.')