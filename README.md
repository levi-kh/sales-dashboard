# Sales Data Dashboard

This is a simple interactive sales dashboard built with Python and Streamlit. It was developed as the final project for CMPSC 462 – Data Structures.



## Objective

The goal of this project is to build a simple interactive sales dashboard that helps users explore data from different perspectives.  

It combines a tree-based view to show hierarchical structure and a graph-based view to reveal relationships between products.  

The objective is to turn raw sales data into clear, visual insights that are easy to understand, using data structures such as trees and graphs we learned in CMPSC 462.



## Dataset

The dataset I used for this project includes the following columns:

- Order ID  
- Region  
- Category  
- Sub-Category  
- Sales  
- Profit  


---

## 1. Tree-Based View

This part shows the data in a hierarchy using a treemap. Products are grouped by category and sub-category.   
Bigger and darker blocks mean higher sales, lighter ones mean lower sales.

It gives a quick overview of which categories are performing well in each region.



## 2. Graph-Based View

This part shows how products are related.

If two items are bought in the same order, they are connected.  
Items that are often bought together appear closer, while unrelated ones stay further apart.



## 3. Summary Stats

This section shows some basic numbers for the selected region:

- Total sales  
- Best-selling items  
- Lowest-performing items  
