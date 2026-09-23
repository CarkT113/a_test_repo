package com.carlos.firstmaven;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Reader;
import java.util.List;
import java.io.IOException;
import java.nio.file.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Hello world!
 *
 */
@RestController
@SpringBootApplication
public class App {
//    public static void main( String[] args )
//    {
//        System.out.println( "Hello World!" );
//    }
	
	private String toJson(final String line)
	{
		String jsonLine  = line;
		JSONObject jsonObject2 = new JSONObject();
		jsonObject2.put("product", "Laptop");
        jsonObject2.put("price", 1200.50);
        jsonObject2.put("inStock", true);
        jsonObject2.put("TransactionID", "TAC1201");
        String jsonString2 = jsonObject2.toString(2);
		return jsonString2;
	}	
	@RequestMapping("/test1")
	String test1MethodName(@RequestParam(name = "fromDt", required = true, defaultValue = "today") String fromDt) {
		// (1) get fromDt and toDt, if today then get current date in yyyymmdd
		// (2) get csv file from .... location ... find rows between from and to dates
		// (3) format as json, return to the caller
		return "Hello World! "+fromDt+" "+toJson("I am test only");
	}
	
	// choose filepath based on url category
	
	// "C:\\Software\\eclipse\\FirstSpringBoot\\firstmaven\\countries.csv"
	
	// NOTE: Check and update file location each time importing the package
	
	static String fileCountries = "C:\\Software\\SpringBoot\\FirstSpringBoot\\firstmaven\\countries.csv";
	static String fileStaffs = "C:\\Software\\SpringBoot\\FirstSpringBoot\\firstmaven\\testinputfor.csv";
	static String fileFX = "C:\\Software\\SpringBoot\\FirstSpringBoot\\firstmaven\\f11.1-data.csv";
			
	// C:\Software\SpringBoot\FirstSpringBoot\firstmaven
	
	// static String fileInterestRate = "C:\\Software\\SpringBoot\\FirstSpringBoot\\firstmaven\\InterestRateAndYield_20251103.csv";
	
	private String toCSV(final String item)	{
				
		JSONObject jsonObject3 = new JSONObject();
		String jsonString = new String();
		String search = item;
		String filePath = new String();
		int count = 1;
		int linesToSkip = 0;
		switch (search) {
		case "StaffRecord":
			filePath = fileStaffs;
			break;
		case "Country":
			filePath = fileCountries;
			break;
		case "FXrates":
			filePath = fileFX;
			linesToSkip = 10;
			break;
		case "InterestRate":
			String fileInterestRate = new String();
			
			PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:InterestRateAndYield*.csv"); // Matches all .txt files
			  // PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:dir/**/*.java"); // Matches all .java files in 'dir' and its subdirectories

			String basedirectory = "C:/Software/SpringBoot/FirstSpringBoot/firstmaven";
			Path basePath = Paths.get(basedirectory);
			try (Stream<Path> paths = Files.find(basePath, Integer.MAX_VALUE, (path, attr) -> matcher.matches(path.getFileName()))) {
				
				List<Path> pathList = paths.collect(Collectors.toList());
				
				fileInterestRate = pathList.toString();
				fileInterestRate = fileInterestRate.substring(1,fileInterestRate.length()-1);
				System.out.println(fileInterestRate);
				System.out.println(fileInterestRate.substring(basedirectory.length()+1,fileInterestRate.length()));
				
				} catch (IOException e) {
			      e.printStackTrace();
				}

			filePath = fileInterestRate;
			linesToSkip = 10;
			break;
		}
		
		try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
				for (int i = 0; i < linesToSkip; i++) {
	                reader.readLine();
	            }
			try (CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.builder()
			.setHeader()	
			.setAllowMissingColumnNames(true)
			.build()
            .withFirstRecordAsHeader() // Treats the first record as headers
            .withIgnoreHeaderCase()    // Ignores case when matching header names
            .withTrim())) {
				// Trims leading/trailing whitespace from values
				List<String> headers = csvParser.getHeaderNames();				//find the file's header
				System.out.println(headers);
				List<CSVRecord> csvRecords = csvParser.getRecords();
				for (CSVRecord csvRecord : csvRecords) {
					JSONObject requestItem = new JSONObject();
					
					for (String header:headers) {								//auto find non empty header and populate fields
						if (header.length() > 0) {
							String headerItem = csvRecord.get(header);
							requestItem.put(header,headerItem);	
						}
						else {}
					}
				jsonObject3.put("ItemRecord"+count,requestItem);
				count+=1;	
				}
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			jsonString = jsonObject3.toString();				
			} catch (IOException e) {
           System.err.println("Error reading CSV file: " + e.getMessage());
           System.err.println("Displaying all available data.\n");
				}	
		//System.out.println(jsonObject3);
		
		Object NestedjsonObject3 = new Object();
		
		try {
			NestedjsonObject3 = jsonObject3.get(search); //specific staff
			System.out.println(NestedjsonObject3);
			jsonString=NestedjsonObject3.toString();
		} catch (JSONException e) {
			System.out.println("cannot find the specific user. Reason: "+ e.getMessage());
			// System.out.println(jsonObject3);
		}
		//NestedjsonObject3.toString();
		
		return jsonString;
				 
	}
	
	@RequestMapping("/readCSV")
	String readCSV(@RequestParam(name = "category", required = true, defaultValue = "null") String category) { //@RequestParam(name = "fromDt", required = true, defaultValue = "today") String fromDt
		//@RequestParam(name = "Record", required = false, defaultValue = "") String record
		// (1) get fromDt and toDt, if today then get current date in yyyymmdd
		// (2) get csv file from .... location ... find rows between from and to dates
		// (3) format as json, return to the caller
		return toCSV(category);
	}
		
	public static void main(String[] args) {
		SpringApplication.run(App.class, args);
	}
}
