## Description
This task was to redesign one of the company's websites ([talluri.technologies.com](http://talluritechnologies.com/)). The old site was powered by WordPress and was several years old. Each intern was to submit a redesign with the following constraints:
 - A static website that has the same content as the original
 - Must be written in HTML/CSS/JS

## Technologies
- Bootstrap
- jQuery
- PostMail 

## Process and challenges
I found that Bootstrap's ready-made elements were most suitable for quickly recreating the structure of the original site. I watched a two-hour-long tutorial to get acquainted with the library and all its features. In my site I include carousels, alerts, grids, and many other Bootstrap elements. I also employed the FontAwesome CDN in several areas. For instance, in the "Contact" page I use it to display a letter and phone icon.

Because the project was not so technically rigorous, I treated it as an exercise in UX/UI design. These subjects have always been relatively challenging for me, and I found this project educational. When I created the site most of my time was spent searching for ways to make information as accessible as possible. I often did this by restructuring the site's elements. 

For example, in the original site each feature of the company's product was listed on a separate page. (Each page had only about one paragraph of text.) This meant that the user was forced to poke around and click several times to read about all the product's capabilites. I opted to move all this content to a single page, and use an accordian to organize the information in an intuitive manner. (I also added "jump" links to make it easier for the user to reach a certain topic from the home page.)

This project also made be mindful of responsive design. I frequently used Chrome developer tools to simulate a mobile phone, and I would adjust my elements to make sure they appeared properly on smaller screens.

While working I frequently edited the navigation bar and footer. Sometimes I would add links to new pages, and other times I would change the CSS. This quickly became frustrating: every edit meant I had to copy and paste the change to every single HTML file in my project. To follow the DRY principle, I learned how to use jQuery to import a navbar and footer from template files into a given HTML file on page load. I used a script to use the current URL path to dynamically identify and highlight the relevant navbar link.
