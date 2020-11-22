# Testing 

## Testing User Stories


### Navbar

- **User Story**
1. As a First Time Visitor, I want to easily navigate the app using the navbar.
3. As a First Time Visitor, I want to be able to navigate to different parts of the site and view the information that it has to offer.


#### Test
- Check the navbar stands apart clearly from the hero images and other content of site
- Click on all links to make sure navbar remains present on each individual page. 
- Click on all links in navbar and make sure that all urls are working.
- Click on all links and make sure they got to intended pages.
- The navbar stays present at the top of the page as you scroll throught the content of the pages.
- Check that content is relevant to the pages heading and/or subheading.
   
####  Results 
- Navbar sits above the delivery banner and under the search engine with enough surrounding whitespace so its is clearly visable.
- Cursor turns to a pointer when hoovered over links to show the user they are on a link.
- As each link is clicked the navbar does not move and stays present no matter which page is being viewed.
- Each page is linked propely and every nav-link goes to the intended page.
- All links work there are no broken urls in the navbar.
- All information relates to the pages headings and or subheadings.

#### Bugs/Improvements
- There are no hobver elements on the nav-links to signify to the user that they are hovering on a nav-link

#### Fixes
- 


- **User Story**
2. As a First Time Visitor, I want to be able to easily find and look through the different products the shop has to offer without the obligation of registering an account.
8. As a First Time Visitor, I want to be able to use the search engine to find different products I might want to buy.

#### Test
- Use the site without being logged in and got the shop section.
- See if all products ae displayed.
- Click on all products to check they open and display correct information.
- Use the query filtering in the shop section to seperate the categories of the products.

#### Results 
- User can navigate using the navbar to the shop section without being logged in.
- All the products from the database are displayed in this section.
- Once clicked all products open to to display details on the product. Alll information is correct from what has been input into the datavbase.
- The query filtering works and displays the correct categories adn place the correct products within these categories.
- If the user types somehing not applicable to the site they will be taken to the shop/products page where there is another query filter that allows the user to search by the categories the site offers.

#### Bugs/Improvements
- The horizontal rule on the product cards is not always in the sam eplace due to the amount of text on each card.

 #### Fixes
- 


- **User Story**
4. As a First Time Visitor, I want to be able to place products into my cart and browse the other items.
5. As a First Time Visitor, I want to be able to place numerous products in my basket as well as multiple amounts of products.

#### Test 
- Place a single item in cart.
- Place single item in cart and browse other pages of the site.
- Place multiple items in cart.
- Place multiople items in cart and brows other pages of the site.
- Place every single item in cart.
- Place every single items in cart and brows other pages of the site.
- Try and 100000 of the same item in the cart.
- Try and place -1 items in the cart.

#### Results
- Without being logged a user is able to place an item into thier cart and then navigate to all other pges of the site with the item still thier cart.
- Without being logged in a user can place multiple items into thier cart and navigate to all areas of the site with the items remaining in tier cart.
- Without being logged in a user can place all items into thier cart and navigate to all areas of the site with the items remaining in tier cart.
- Also the user can place different amounts of each item into thier cart and still navigate to to all areas of the site with the items remaining in their cart.
- All items remained in the cart and were displayed at the checkout.
- Trying to place anything over 99 of the same item in the cart results in an derror and message stating 'value must be less or equal to 99' and nothing in placed in the cart.
- Trying to place anything over -1 items in the cart results in an derror and message stating 'value must be less or equal to 99' and nothing in placed in the cart.

#### Bugs/Improvements
- The number of each of item the user has in thier account is not displayed. The total cost of  each item is and its totl value.

#### Fixes
-

- **User Story**
7. As a First Time Visitor, I want to be able to safely securely purchase my items from the checkout.

#### Test 
- With item(s) in cart checkout using correct information to fill out the delivery details (4242 4242 4242 4242 242 - as the card number D.O.B and ccv).
- With item(s) in cart checkout with out filling out one or more of the required fields.
- With item(s) in cart checkout with out using @ or .com/org  on te email field.

#### results
- When all fields are filled out correctly in the delivery information everything runs smoothly and an message a mesage is displayed staing 'Order successfully processed! Your order number is 5977DAEF6817440D81F1F88CF3BA803C. A confirmation email will be sent to Test@gmail.com.'
- If a user tries to checkout without filling in the required fields a message pops up to let he user know they must fill in this field. 
- If a user tries to checkout without using the @ symbol or a .com/org a message will diplay indicating the error.
- If a user trie to checkout msiplacing the . or using , instead they will get an error message.

#### Bugs/Improvements
- A user can check out with any email as long as it has the correct form of a letter@letter.letter (e/g j@s.k -would allow the user to checkout).

#### Fixes 
- Not sure if this is a fixable problem or relevant to this assignment.













