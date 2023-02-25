```python
import cv2 as c
from matplotlib import pyplot as plt
```


```python
img_wall=c.imread('wall.jpg')
img_text=c.imread('txt_img.jpg')
```


```python
plt.imshow(c.cvtColor(img_wall,c.COLOR_BGR2RGB))
```




    <matplotlib.image.AxesImage at 0x201e6b73310>




    
![png](output_2_1.png)
    



```python
plt.imshow(c.cvtColor(img_text,c.COLOR_BGR2RGB))
```




    <matplotlib.image.AxesImage at 0x201e8788c90>




    
![png](output_3_1.png)
    



```python
img_leaf=c.imread('leaf.jpg')
plt.imshow(c.cvtColor(img_leaf,c.COLOR_BGR2RGB))
```




    <matplotlib.image.AxesImage at 0x201e8557e90>




    
![png](output_4_1.png)
    



```python
   leaf_grayscale=c.cvtColor(img_leaf,c.COLOR_BGR2GRAY)
```


```python
plt.imshow(leaf_grayscale,cmap='gray')
```




    <matplotlib.image.AxesImage at 0x201e6aa0c90>




    
![png](output_6_1.png)
    



```python
retval,leaf_mask=c.threshold(leaf_grayscale,10,255,c.THRESH_BINARY)
```


```python
plt.imshow(leaf_mask,cmap='gray')
```




    <matplotlib.image.AxesImage at 0x201e6b70c90>




    
![png](output_8_1.png)
    



```python
add_img=c.add(img_wall,img_text,mask=leaf_mask)

```


```python
plt.imshow(c.cvtColor(add_img,c.COLOR_BGR2RGB))
```




    <matplotlib.image.AxesImage at 0x201ea028c90>




    
![png](output_10_1.png)
    

