package view;

import java.util.ArrayList;

public class Product{
    private String product;
    private String description;
    private ArrayList<String> founders;
    private String patentNum;
    private String orgin;
    private String status;
    private String company;

    public Product(){
        product = "none";
        patentNum = "none";
        orgin = "none";
    }
    public Product(String p, String pN, String o){
        product = p;
        patentNum = pN;
        orgin = o;
    }

    public String getProductName(){
        return product;
    }
    public String getDesc(){
        return product;
    }
    public String getProductName(){
        return product;
    }
    public String getProductName(){
        return product;
    }
    public String getProductName(){
        return product;
    }
    public String getProductName(){
        return product;
    }
    public String getProductName(){
        return product;
    }

    public void setDescription(String d){
        description = d;
    }
    public void setStatus(String s){
        status = s;
    }
    public void addFounder(String name){
        founders.add(name);
    }
    public void setCompany(String comp){
        company = comp;
    }
}