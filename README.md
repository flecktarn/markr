# markr

A basic flask server that lists and displays markdown files. 

## Dependencies:
- [Flask/jinja](https://flask.palletsprojects.com/en/1.1.x/)
- [Python markdown](https://python-markdown.github.io/reference/)
- [Bootstrap](https://getbootstrap.com/)
- [Zephyr Bootstrap theme](https://bootswatch.com/zephyr/)
- [highlight.js](https://highlightjs.org/)

## How to use:
To use the server, simply run it and navigate to the main page.

---

![image](https://user-images.githubusercontent.com/53770200/117810071-4c54bd00-b2a2-11eb-8331-6f987365fb31.png)

---

Files are shown in an index, clicking on one will enter markdown view, from there you can return to the index or view the raw file.

---

![image](https://user-images.githubusercontent.com/53770200/117810204-70180300-b2a2-11eb-8a17-c46cbcb0c92f.png)

---
To add files to the server, put them in the **documents** folder.

markr will attempt to find a title based on the first line of text it finds in the file, you can also add a description by adding an italicised second line to the file, which will be displayed in the index.


**example.md:**

```
#I'm a title!
_I'm a description :D_
```
---

![image](https://user-images.githubusercontent.com/53770200/117811030-73f85500-b2a3-11eb-9c36-e3d5b429bb0a.png)
