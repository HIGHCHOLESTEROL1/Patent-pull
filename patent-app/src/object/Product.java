package object;

import java.util.ArrayList;
import java.util.Map;
import java.util.Set;

public class Product{
    private String product;
    private String description;
    private Map<String, ArrayList<String>> founders;
    private String patentNum;
    private String orgin;
    private String status;

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
        return description;
    }
    public ArrayList<String> getFounders(String company){
        return founders.get(company);
    }
    public Set<String> getCompany(){
        return founders.keySet();
    }
    public String getOrgin(){
        return orgin;
    }
    public String getPatentNum(){
        return patentNum;
    }
    public String getStatus(){
        return status;
    }

    public void setDescription(String d){
        description = d;
    }
    public void setStatus(String s){
        status = s;
    }
    public void addFounder(String company, String name){
        if (founders.get(company) == null){
            founders.put(company, new ArrayList<String>());
        }
        founders.get(company).add(name);
    }
}