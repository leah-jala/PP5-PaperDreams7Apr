# Note regarding project development and commits

While developing this project, I had wanted to use djmoney with the intention of later implementing functionality that would recognize a user's locale and update the currency.
I had to make many changes to my project to accommodate djmoney. In the end, it created problems that I could not overcome, related to adding products to the shopping basket and calculating the subtotals and totals. I thought I could uninstall djmoney, undo previous changes and carry on. Even though I had unstalled the package and altered the model, there continued to be a conflict and some presense of a djmoney related currency field. I tried deleting all my products from the database and getting rid of the field in the shell, but it didn't work and I decided I was making things worse with all the fixes I was trying to make. In the end, I started with a fresh repo. The consequence is that the commit history does not reflect the true development of the project. This means that in the early commits of this repo there are, for example, settings and fields including in html files, that don't make sense to be there as I had to minimize the amount of time I would lose by needing to begin with a fresh repo.

Below, I include links to the commit history of the first version of this project

- Commits 1-18 of this repo reflect me trying to get my project set up to the point I left off up, which is up to the point of the product_detail page.
- Commits 19 - ? of this repo relate to the shopping bag page. I will reuse the javascript I wrote in first version.

There are few differences between the first and second versions. I experimented by adding a title and header to the products_datail page that previously was not there. 

Together these commits relate to comments 1-59 in the first repo [NEW-paperdreams](https://github.com/leah-jala/NEW-paperdreams/commits/main). These commits show the incremental development of the base and index files, the products page and the product detail page with related javascript, as well as early attempts to include a wishlist, and to use djmoney. It also reveals problems that I encountered, particularly with the active classes on the category buttons on the products page, in particular the "All Artworks" button. I also tried to include functionality that would prevent a user from adding more products than what is available in the database. It was not functioning correctly at the time of creating the new repo. The button would disable when the user reached the maximum avaiable products, but the user could add them multiple times. 

#Technology
[https://www.xml-sitemaps.com/](Online sitemap generator)
[https://search.google.com/search-console/about](Register sitemap)

# Credits
[Shopping bag Bootstrap/Html](https://mdbootstrap.com/docs/standard/extended/shopping-carts/) adapted from MDB
[Bootstrap Toasts](https://getbootstrap.com/docs/4.3/components/toasts/) - reviewed this but used the Boutique Ado html.  The tutorial had taken the toast html direct from Bootstrap and added some extra styling. For the sake of speed I have borrowed this.
[Contact Page](https://www.bootdey.com/snippets/view/contact-page-section#html)
Django Documentation
- [Understanding Widgets](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/)
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)

# Notes

The setting "MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'" is not usually required, but it was in the case of this project due to using Git Pod, according the the Boutique Ado Tutorial.