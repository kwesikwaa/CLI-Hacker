this little experiment took me on an interesting journey
it begun with an interest in making hacker screen terminals in movies.

inital interest was to do it all with straightforward CLI-like feel. it took me to take a serious look into the python rich library.
the rich library has components that i will always use for other things, like its prompt, confirm and logging features. however the sweetest part of it; layout doesnt fit my use case. i couldnt find a way to refresh only a part of the layout without affecting the entire layout.
it got me to look into #curses#. Curses provide various windows to do exactly what i was looking for however it looks needlessly cumbersome with its styling, and which data to pass through. 
finally looked into textualize from the maker of the rich library. it turns out to be the perfect frontend for the backend developer. doesnt come with the css uncertainity and all the framework brouhaha. just code away. 
in one night i had familiarised myself with librairies not only for python but also bubble for golang. and so because i can, i decided to replicate everything in go as well.
