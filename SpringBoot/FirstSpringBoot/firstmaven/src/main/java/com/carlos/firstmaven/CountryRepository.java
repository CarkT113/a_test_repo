package com.carlos.firstmaven;

import java.sql.*;

import org.json.JSONObject;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import com.sun.tools.javac.Main;

import java.util.List;

@Component("countryRepositoryByName")
public class CountryRepository {
	
	static final String DB_URL = "jdbc:mysql://192.168.1.121:3306/mysqlbusinessdata";
    static final String USER = "carlos";
    static final String PASS = "carlos123";
        
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;
    
    String jsonString = new String();
    JSONObject jsonObject5 = new JSONObject();
    JSONObject requestItem = new JSONObject(); //container for query request
    int count = 1;
    public Statement getConnection() {
    	try {
    		Class.forName("com.mysql.cj.jdbc.Driver");
            // Open a connection
    		System.out.println("Connecting to database...");
    	    conn = DriverManager.getConnection(DB_URL, USER, PASS);
    	    System.out.println(conn);
            // Execute a query
            System.out.println("Creating statement...");
            stmt = conn.createStatement();	
            System.out.println(stmt);
    	} catch (SQLException se) {
            // Handle JDBC errors
            se.printStackTrace();
        } catch (Exception e) {
            // Handle Class.forName errors
            e.printStackTrace();
        }
    	System.out.println("Connection Successful!");
    	return stmt;
    }

    
    public void closeConnection() {
    	// Close resources in reverse order of creation
    	try {
            if (rs != null) rs.close();
        } catch (SQLException se2) {
            se2.printStackTrace();
        }
        try {
            if (stmt != null) stmt.close();
        } catch (SQLException se2) {
            se2.printStackTrace();
        }
        try {
            if (conn != null) conn.close();
        } catch (SQLException se) {
            se.printStackTrace();
        }
    }
    
    public void resetCounter() {
    	count = 1;
    }
    
	public String findAllCountries() {
		
		try {
            String sql = "SELECT country_name,country_code FROM countries;";
            System.out.println(sql);
            rs = getConnection().executeQuery(sql); // execute query and get data
            // Process the result set
            while (rs.next()) {
                // insert column
                String countryName = rs.getString("country_name");
                String countryCode = rs.getString("country_code");
                //int age = rs.getInt("age");
                System.out.println("Country Name: " + countryName + ", Country Code: " + countryCode);
                requestItem.put("country_name", countryName);
                requestItem.put("country_code", countryCode);

                jsonObject5.put("ItemRecord"+count,requestItem);
                count+=1;
            }
            
            jsonString = jsonObject5.toString();
            
		} catch (SQLException se) {
            // Handle JDBC errors
            se.printStackTrace();
        } catch (Exception e) {
            // Handle Class.forName errors
            e.printStackTrace();
        }
		closeConnection();
		resetCounter();
		return "Connection Successful!"+jsonString;//"I am from findAll for "+fromDt+" [ "+getRecords(fromDt);
	}
	
	private String getRecords(final String fromDt) {
		// (1) make a connection to mySql
		// (2) query and get list of records using parameters
		// (3) format the records into something and return (for this case as a string)
		// (4) close connection
		return "I am records as json"; 
	}
	
	public static void main(String[] args) {
    }
}