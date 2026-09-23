package com.carlos.firstmaven;

import jakarta.persistence.*;

@Entity
@Table(name = "countries")
public class Country {
	
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // MySQL-friendly
    private Integer id;
    private String country_name;
    private String country_code;
    
    public Country(String country_name, String country_code) {
        this.country_name = country_name;
        this.country_code = country_code;
    }

    // getters & setters
    public Integer getId() { return id;}
    public void SetId(Integer id) { this.id = id; }
    
    public String getCountryName() { return country_name; }
    public void setCountryName(String country_name) { this.country_name = country_name; }

    public String getCountryCode() { return country_code; }
    public void setCountryCode(String country_code) { this.country_code = country_code; }
}

