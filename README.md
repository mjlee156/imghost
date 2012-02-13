imghost
=======

Introduction
------------

Imghost is a django webapp for hosting and sharing images.  It is designed to 
be "semi-private" so that users of the webapp can upload images and share them, 
but a listing of all images is not available publicly.

Features
--------

* Upload images
* List all images
* Link to mirror to imgur (on list page)
* Duplicate protection (new images with matching md5sum will be discarded and the existing image link will be provided)
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) layout

Planned Features
----------------

* Multi-user friendly
* Easier deployment
* Mobile friendly listing
* Mobile upload app (android)

Deploying
---------

More on how to do this later.  Currently I use a combination of mod_wsgi for my
primary instance of the app, and gunicorn or the django server for development.

I use mysql for my "production" instance, and sqlite3 while developing.  Postgresql
and others should work just fine though, there isn't any magic going on.


License
-------

imghost is licensed under the MIT license.  See ```LICENSE``` for full details.

