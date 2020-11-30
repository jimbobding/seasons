# Testing 

## Testing User Stories


- **User Story**
1. As a First Time Visitor, I want to easily navigate the app using the navbar.
3. As a First Time Visitor, I want to be able to navigate to different parts of the site and view the information that it has to offer.


#### Test
- Check the navbar stands apart clearly from the hero images and other content of the site
- Click on all links to make sure navbar remains present on each page. 
- Click on all links in the navbar and make sure that all URLs are working.
- Click on all links and make sure they got to intended pages.
- The navbar stays present at the top of the page as you scroll through the content of the pages.
- Check that content is relevant to the pages heading and/or subheading.
   
####  Results 
- Navbar sits above the delivery banner and under the search engine with enough surrounding whitespace so it is visible.
- Cursor turns to a pointer when hovered over links to show the user they are on a link.
- As each link is clicked the navbar does not move and stays present no matter which page is being viewed.
- Each page is linked properly and every nav-link goes to the intended page.
- All links work there are no broken URLs in the navbar.
- All information relates to the pages headings and or subheadings.

#### Bugs/Improvements
- There are no hover elements on the nav-links to signify to the user that they are hovering on a nav-link

#### Fixes
- 

- **User Story**
2. As a First Time Visitor, I want to be able to easily find and look through the different products the shop has to offer without the obligation of registering an account.
8. As a First Time Visitor, I want to be able to use the search engine to find different products I might want to buy.

#### Test
- Use the site without being logged in and got the shop section.
- See if all products are displayed.
- Click on all products to check they open and display the correct information.
- Use the query filtering in the shop section to separate the categories of the products.

#### Results 
- User can navigate using the navbar to the shop section without being logged in.
- All the products from the database are displayed in this section.
- Once clicked all products open to display details on the product. All information is correct from what has been input into the database.
- The query filtering works and displays the correct categories and place the correct products within these categories.
- If the user types something not applicable to the site they will be taken to the shop/products page where there is another query filter that allows the user to search by the categories the site offers.

#### Bugs/Improvements
- The horizontal rule on the product cards is not always in the same place due to the amount of text on each card.

 #### Fixes
- This has not been fixed as of yet

- **User Story**
4. As a First Time Visitor, I want to be able to place products into my cart and browse the other items.
5. As a First Time Visitor, I want to be able to place numerous products in my basket as well as multiple amounts of products.

#### Test 
- Place a single item in cart.
- Place the single item in the cart and browse other pages of the site.
- Place multiple items in cart.
- Place multiple items in the cart and browse other pages of the site.
- Place every single item in cart.
- Place every single item in the cart and browse other pages of the site.
- Try and 100000 of the same item in the cart.
- Try and place -1 items in the cart.
- Using the increment and decrement buttons to adjust the number of items in the cart.

#### Results
- Without being logged a user can place an item into their cart and then navigate to all other pages of the site with the item still their cart.
- Without being logged in a user can place multiple items into their cart and navigate to all areas of the site with the items remaining in tier cart.
- Without being logged in a user can place all items into their cart and navigate to all areas of the site with the items remaining in tier cart.
- Also the user can place different amounts of each item into their cart and still navigate to all areas of the site with the items remaining in their cart.
- All items remained in the cart and were displayed at the checkout.
- Trying to place anything over 99 of the same item in the cart results in an error message stating 'value must be less or equal to 99' and nothing is placed in the cart.
- Trying to place anything over -1 items in the cart results in an error message stating 'value must be less or equal to 99' and nothing is placed in the cart.

#### Bugs/Improvements
- Unable to adjust the number of items using decrement/increment buttons, when pressed the number is not incremented but just added straight to cart.

#### Fixes
- The post load javascript script for the increment and decrement items was not being loaded as the script had been cut in half from auto-formatting, I manually reformated the script and it now works.

- **User Story**
7. As a First Time Visitor, I want to be able to safely securely purchase my items from the checkout.

#### Test 
- With item(s) in cart checkout using correct information to fill out the delivery details (4242 4242 4242 4242 242 - as the card number D.O.B and CCV).
- With item(s) in cart checkout without filling out one or more of the required fields.
- With item(s) in cart checkout without using @ or .com/org on the email field.

#### results
- When all fields are filled out correctly in the delivery information everything runs smoothly and a message is displayed stating 'Order successfully processed! Your order number is 5977DAEF6817440D81F1F88CF3BA803C. A confirmation email will be sent to Test@gmail.com.'
- If a user tries to checkout without filling in the required fields a message pops up to let the user know they must fill in this field. 
- If a user tries to checkout without using the @ symbol or a .com/org a message will display indicating the error.
- If a user trie to checkout misplacing the . or using, instead they will get an error message.

#### Bugs/Improvements
- A user can check out with any email as long as it has the correct form of a letter@letter.letter (e/g j@s.k -would allow the user to checkout).

#### Fixes 
- Not sure if this is a fixable problem or relevant to this assignment.


### Returning Visitor Goals

- **User Story**
1. As a Returning Visitor, I want to be able to register an account with the site.

#### Test
- The user has two options to sign in and register an account. Above the main navbar, there is an account section which allows the user to log in and in the about section, there is a CTA which takes the user to the register page.
- Try and register with a bad email address.
- Try a different combination of user names.
- Try different combinations of passwords.
- Try creating an account using an in-use email address.
- Try creating an account using an in use username address.

#### Results 
- Both the register link in the account section and the CTA in the about section worked and takes the user to the register page.
- If a user tries to checkout without using the @ symbol or a .com/org a message will display indicating the error.
- If the user name is shorter than 4 letters a message will display telling the user and will not proceed with the form.
- If a password is not 8 letters or more it will display a message stating 'This password is too short. It must contain at least 8 characters'.
- If a password is too similar to the username a message will display stating 'password is too similar to username.'
- If a password is to common a message will display password is too common.
- A verification email is sent so that a user must use a correct email address to sign up to the site.
- If a user's emails are not the same each time they are typed in an error message will state 'You must type the same email each time'.
- If a user tries to use an email already registered an error message will state 'A user is already registered with this e-mail address.'

- **User Story**
2. As a Returning Visitor, I want the site to be able to remember my delivery details.
2. As a Frequent User, I want to be able to edit and or delete my delivery details.

#### Test
- Register an account.
- Place an order filling in the delivery information and click the save delivery information button.
- Place another order to see if delivery information is saved.
- change delivery information in the second order.
- Go to make a third order and see if the information has changed.
- Go to the profile tab and check information is saved there.
- Try and change the information in the profile tab.

#### Results
- Made an account with a test email.
- Placed order and saved details on return for a second-order my delivery details were saved.
- Placed a third-order and the changes I had made during my previous order had been saved.
- Went to the profile tab and changed the details, received a message confirming the toast and details were changed.
- Went to place a fourth-order, details that were changed in the profile settings had been saved t the order form.
- Logged out of the sie and back in again using the same test profile and the details had been saved.

- **User Story**
3. As a Returning Visitor, I want to be able to look through the subscriptions and learn if it is better value to subscribe.
4. As a Returning Visitor, I want to be able to look through the subscriptions and learn what produce is in season in particular times of the year.
5. As a Returning Visitor, I want to be able to place subscriptions into my cart.

#### Test
- Go to the subscriptions page and view the prices of the subscriptions.
- Look through the information on the subscription page to see if it displays what the user would need.
- Place the subscriptions object into the cart.
- Place multiple subscriptions into the cart.

#### Results
- Navigating to the subscriptions can be done by using the navbar or through a CTA on the about section.
- The subscription page has images and text relating to each season of the year. Each season has a CTA which takes the user to the season detail page.
- The subscription detail page has a hero image which displays the name of the season and the months that fall into that season underneath, the months of the year are also displayed in the blurb of the page along with the fruits and vegetables in season for that season.
- The subscription detail card displays the price of the subscription fr the season as well as the break down of the price per week it will cost.


#### Bugs 
- User is unable to place subscription into the cart.

#### Fixes
- It seems that I was unable to register items in the  subscription model,  separately to the product items. The product Id's were not getting separated and only being read as product ID's, I tried to enter the subscriptions as sub Items so they would have a string relating to the subscription('size') model but this did not work. After spending a few days on this problem and being in constant contact with the course tutors and speaking to my mentor I was still unable to ascertain the problem as they thought the code I had written should have worked.
s time was a factor and I was unable to fix the problem I decided to take a different approach, I folded the subscription('size') model into the products model and then used the category key to separate the subscription('size') items (within the product model) from the original product models. I then pased through the season key which both subscriptions and products shared int the subscription details page. This meant it would display the only the items relted to the season clicked on, E/g if a user clicked on teh winter subscription it would disply 
the products that were related to the winter season. I then added a link at the bottom that took the user to the products page but used a filter so it wouldonl show the subscription ite,s in the product models.
This gave an almost desired result, I will further investigate this issue in my own time to resolve it for future purposes.

- **User Story**
3. As a Frequent User, I want to be able to view the past orders I have made on the site.

#### Test
- Sign in on a registered account and place an order.
- on the same account sign out and sign back in again.
- Navigate to the profie page and click on the order history tab.

#### Result 
- On the order hostory page the past order was displayed.
- Reapeted the process with same profile and also with different test profile and got the same result.

- **User Story**
4. As a Frequent User, I want to be able to easily and safely exit the app.

#### Test
- sign in with an account, sign out of account close down web page and re-open.


- **User Story**
5. As a Frequent User, I want to be able to view the app easily on different devices.

#### Test
- Go through each section of the website using the development tools to check the responsiveness on teh devices it has to offer.
- Check the responsiveness on my personal devices on different web broewsers.
- send t live websites to several friends so they can reveiw the website on various devices.


#### Result 

- The site has been built using [bootstrap 4](https://getbootstrap.com/ )which is a responsive framework. "Bootstrap is a potent front-end framework used to create modern websites and web apps. It's open-source and free to use, yet features numerous HTML and CSS templates for UI interface elements such as buttons and forms".

### Site Owner Goals Goals

add products
- **User Story**
1. As a site owner I want to be able to edit, delete and add products and or change the subscriptions.

#### Test
- Add a product without an image.
- Add a product without an image.
- Edit a product in each individual field.
- Edit a product with incorrect information.
- create a product and add it to the cart 

#### Results
- image was not displaying in the cart for newly added products.
- 404 when adding product 'No Product matches the given query.'
- Adding a product without an image gives a 404 but does add the image

#### Bugs 
- Mistake in the spelling for the no-image jpeg.
- Same in toasts, cart and product detail.
- Had a target blank href to a product's image in the no-image jpeg part.




Editing products

#### Test
- edit a product using incorrect information to submitting a price with over 6 digits
- Edit a product using the correct information.
- Change the product rating to a higher rating than 5

#### Results
- If using more than 6 digits when editing a product an error message will show 'Failed to update the product. Please ensure the form is valid.' as well as an error toast.
- When editing a product with the correct information a success toast will show ' Successfully updated product!' and the product will be updated.

### Going live
 Problems encountered after making the site live.

 - All items in all models were not visible.
 - Some images on the index and about pages were not showing as well as the site logo.
 - Images for my model - items were no showing up.
 

#### Fix 
- I used a manual "dump" of the local (SQLite) data. the steps I took were 
1. Commented out my DATABASE_URL in my env.py file to disable Postgres temporarily, to connect back to SQLite.
2. Then I ran the command - python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json in my terminal to create a db.json file.
3. Then I un-Commented out my DATABASE_URL in my env.py file and restarted my workspace to connect back up with Postgres.
4. Then I ran the command python3 manage.py loaddata db.json that loaded all the files from db.json file and I could now view them on my live site.

- The images on the index and about pages, src = {{ STATIC_URL }} so they were not pointing tho the media folder in amazon s3 bucket, I changed the this to = {{ STATIC_URL }}. This fixed the problem and the images displayed.
- Within the s3 bucket I had accidentally stored some of the images in a folder so it was searching for media > files but the images were media > media > files. I corrected this by removing the file and copying the images directly int the bucket.


#### Functionality Testing

### Navbar
- Click on all of the navebar links.
- Click on all of the links of the hamberger menu.

### Results

- All links go the desired page


### Search engine
#### Test
- Search for items that are not in the database.
- Search for key words that are in the items.
- Search for words that are nothing to do with anything in the database.

### Results
- Searched for word box all the products that are boxes showed on the page.
- Searched for the word subscription all the products that are subscriptions showed on the page.
- Searched for bacon no results were shown. 'Products Home | 0 Products found for "bcon"'


### Payment forms
 #### Test
 - To test the payment form I used a variety of difeer combinations of leaving certain fields blank.
 - I also used a variety of different countries. But not all of them,
 - I used the code 4242 4242 4242 4242 and then an expiry date that is valid and any 3 letter ccv.

 #### Results
 - The only problems I encountered were leaving  name, email street adrres 1 and country fields emepty.
 - The email field had to appear as if a legitame email was being used o @. com is required.
 - There have been problems with some countries and the use of postal address is needed. I have attatched and alternative trial key to in case this problem is encountered. = 4012888888881881.
 [Stripe Elements forcing a postal code](https://stackoverflow.com/questions/46737413/stripe-elements-forcing-a-postal-code).


[Back to README](https://github.com/jimbobding/seasons/blob/master/README.md)