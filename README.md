## Sentiment Analysis of Restaurant Reviews

![Alt text](http://www.clarabridge.com/wp-content/uploads/2016/10/Sentiment.jpg)

For Sentiment Analysis following are languages/ tools are used

  - Python
  - Spark 
  - NLTK Natural Language Tool Kit
  - Matplotlib for plotting

Dataset is from:
  - Yelp Restaurant Reviews
  - Curanted Dataset


Naive Bayes Weights to each word based on training dataset  

```
          contains(rude) = True           negati : positi =     14.3 : 1.0
     contains(wonderful) = True           positi : negati =     10.9 : 1.0
       contains(amazing) = True           positi : negati =      7.3 : 1.0
     contains(delicious) = True           positi : negati =      7.1 : 1.0
         contains(loved) = True           positi : negati =      6.9 : 1.0
       contains(manager) = True           negati : positi =      6.4 : 1.0
         contains(asked) = True           negati : positi =      6.4 : 1.0
     contains(manhattan) = True           positi : negati =      6.3 : 1.0
     contains(authentic) = True           positi : negati =      5.6 : 1.0
     contains(fantastic) = True           positi : negati =      5.3 : 1.0
     contains(attentive) = True           positi : negati =      5.0 : 1.0
          contains(cozy) = True           positi : negati =      5.0 : 1.0
          contains(meal) = True           positi : negati =      4.6 : 1.0
         
```
