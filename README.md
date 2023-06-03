# Plugins for Labelme
### This is a collection of plugins for [Unofficial Labelme Fork](https://github.com/leonelhs/labelme/)

<h1 align="center">
  <img src="https://drive.google.com/uc?export=view&id=1-jyUPeXOx7p3JAbdorKUD5cOHveOTh6D"/><br/>labelme
</h1>

## Plugins:

### Make Contour

This plugin uses an AI web service to auto generate contour body shapes of a person picture.

### How to use it:
Before to run the plugins is mandatory to install **Faceshine web server**.

**Faceshine** will provide a Pytorch Resnet101 segmentation API

```shell
pip install faceshine
faceshine
```

Once the server is running, clone or download this repo and proceed to install the `makecontour.plugin` file on Labelme

<img src="https://drive.google.com/uc?export=view&id=1IgaBj4KsjM6wzeUR5tSYNnei205ZSEJ6"/>

<img src="https://drive.google.com/uc?export=view&id=1Ywy-9FVPXyYYomQm6gGuViiuSHDxZNlc"/>

<img src="https://drive.google.com/uc?export=view&id=16wzxNm8ztLsCI5BT1D89quaB6gwGz8F6"/>

<img src="https://drive.google.com/uc?export=view&id=19PjxyFnHzSprAGfj9QIsqNISs45Rq5Jh"/>


[comment]: <> (Suggested for keep original reference through forks)
<p align="center">
    Forked from:<a href="https://github.com/leonelhs/labelme-plugins">Labelme Plugins</a>
</p>