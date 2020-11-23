# Testing 

## Testing User Stories


### Navbar

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
- 

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

#### Results
- Without being logged a user can place an item into their cart and then navigate to all other pages of the site with the item still their cart.
- Without being logged in a user can place multiple items into their cart and navigate to all areas of the site with the items remaining in tier cart.
- Without being logged in a user can place all items into their cart and navigate to all areas of the site with the items remaining in tier cart.
- Also the user can place different amounts of each item into their cart and still navigate to all areas of the site with the items remaining in their cart.
- All items remained in the cart and were displayed at the checkout.
- Trying to place anything over 99 of the same item in the cart results in an error message stating 'value must be less or equal to 99' and nothing is placed in the cart.
- Trying to place anything over -1 items in the cart results in an error message stating 'value must be less or equal to 99' and nothing is placed in the cart.

#### Bugs/Improvements
- The number of each item the user has in their account is not displayed. The total cost of each item is and its total value.

#### Fixes
-

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
- The user has two options to sign in and register an account. Above the main navnar there is an account section wicch allows the user to look in and in te about section there is a cta which takes the user to the register page.
- Try and register with a bad email address.
- Try different combination of user names.
- Try different combinations of passwords.
- Try creating an account using an inuse eamail address.
- Try creating an account using an inuse username address.

#### Results 
- Both the register link in the account section and the CTA in the about section worked and takes the user to the register page.
- If a user tries to checkout without using the @ symbol or a .com/org a message will display indicating the error.
- If the user name is shorter than 4 letters a message will display tellling the user and will not proceed with the form.
- If a password is not 8 letters or more it will display a message stating 'This password is too short. It must contain at least 8 characters'.
- If a password is too similar to the username a message will display stating 'password is to similar to username.'
- If a password is to common a message will dis[lay password is to common.
- A verification email is sent so that a user must use a correct email address to sign up to the site.
- If a users emails are not the same each time they are typed in an error message wil state 'You must type the same email each time'.
- If a user tries to use an email already registered an error message will state 'A user is already registered with this e-mail address.'

- **User Story**
2. As a Returning Visitor, I want the site to be able to remember my delivery details.
2. As a Frequent User, I want to be able to edit and or delete my delivery details.

#### Test
- Register an account.
- Place an order filling in the delivery information and click the save delivery information button.
- Place another order to see if delivery information is saved.
- change delivey information in second order.
- Go to make a third order and see if the information has changed.
- Go to profile tab and check information is saved there.
- Try and change information in profile tab.

#### Results
- Made an account with a test email.
- Placed order and saved details on return for a second order my delivery details details were saved.
- Placed a thrid order and the changes I had mde during my previous order had been saved.
- Went to the profile tab and changed the details, recieved a message confirming the toast and details were changed.
- Went to place a fourth order, details that were changed in the profile settings had been saved t th order form.
- Logged out of the sie and back in again using the same test profile and the detauil shad been saved.

- **User Story**
3. As a Returning Visitor, I want to be able to look through the subscriptions and learn if it is better value to subscribe.
4. As a Returning Visitor, I want to be able to look through the subscriptions and learn what produce is in season in particular times of the year.
5. As a Returning Visitor, I want to be able to place subscriptions into my cart.

#### Test
- Go to subscriptions page and view the prices of the subscriptions.
- Look through the information on the subscription page to see if it dispalys what the usr would need.
- Place the subscriptions object itno the cart.
- Place multiple subscription into the cart.

#### Results
- Navigating to the subscriptions can be done by using the navbar or through a CTA on the about section.
- The subscription page has images and text realting to each season of the year. Each season has a CTA which takes the user to the season detail page.
- The subscription detail page has a hero image which dispalys the name of the season and the months that fall in to that season underneath, the months of the year are aso dispayed in the blurnb of the page along with the fruits and vegetables in season for that season.
- The subscription detail card displays the price of the subscription fr the seson as well as th ebek down of the price per week it will cost.


#### Bugs 
- User is unable to place subscription into the cart.

#### Fixes
- Am urrently resolving this issue



[Back to README](https://github.com/jimbobding/seasons/blob/master/README.md)

    1. Once a user has registered with the site, they have the option to save their details when they originally input them whilst placing an order.
3. As a Returning Visitor, I want to be able to look through the subscriptions and learn if it is better value to subscribe.
    1. In the subscriptions detail page the subscriptions card display the price of the subscriptions whilst also displaying the price per box value they are receiving.
4. As a Returning Visitor, I want to be able to look through the subscriptions and learn what produce is in season in particular times of the year.
    1. All of the seasonal produce is displayed in the subscription detail page. All produce related to a certain season is in within that season's page which can be accessed by a CTA.
    2. The months of that season are also provided within the subscription detail page.




    1. The profile page has a change information CTA at the bottom of the page, that allows the user to edit each line of their delivery information.
3. As a Frequent User, I want to be able to view the past orders I have made on the site.
    1. Within the profile page the user can view all past orders as long as they are registered with the site. 
4. As a Frequent User, I want to be able to easily and safely exit the app.
    1. The user can easily enter the account tab and log out of the site. This will end their session.
5. As a Frequent User, I want to be able to view the app easily on different devices.
    1. The site has been built using [bootstrap 4](https://getbootstrap.com/ )which is a responsive framework. "Bootstrap is a potent front-end framework used to create modern websites and web apps. It's open-source and free to use, yet features numerous HTML and CSS templates for UI interface elements such as buttons and forms".


### Site Owner Goals Goals
1. As a site owner I want to be able to edit, delete and add products and or change the subscriptions.
2. As a site owner I want to receive emails from the users when they fill out the contact form so that I can reply to them satisfying users queries.









