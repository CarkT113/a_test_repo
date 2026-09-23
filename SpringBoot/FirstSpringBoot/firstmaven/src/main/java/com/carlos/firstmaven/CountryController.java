package com.carlos.firstmaven;

import com.carlos.firstmaven.CountryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;
import java.util.List;

@RestController
@RequestMapping(path="/country")
public class CountryController {
	
	@Autowired(required = false) // bean
	private CountryRepository countryRepositoryByName;

	// Home Page
	@GetMapping(path="/")
	public String welcome() {
		System.out.println(Country.class);
		System.out.println(CountryRepository.class);
		System.out.println(countryRepositoryByName.getConnection());
		return "<html><body><h1>WELCOME</h1></body></html>";
	}

	// Get All Countries
	@GetMapping(path="allcountries")
	public String getAllCountries() { //List<Country> @RequestParam(name = "fromDt", required = false, defaultValue = "null") String fromDt
		return countryRepositoryByName.findAllCountries();//countryRepository.findAll(); 
	}
	
	// Get A Country
	//@GetMapping(path="/{country_name}")
	//public List<Country> getaCountry(@PathVariable String country_name) {
	//	return countryRepository.findByCountryName(country_name);
	//}

  // read table from MySQL database
  //public List<Country> getAllCountries() {
  //	return countryRepository.findAll();
  //}
  
  
  // Get a Country by a Country Code
  //@GetMapping("/{country_name}")
  //public Country getCountryByCode(@PathVariable String country_code) {
  //    return CountryRepository.findById(country_code)
  //            .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Company not found"));
  // }

  // Create a Company
  //@PostMapping
  //@ResponseStatus(HttpStatus.CREATED)
  //public Company createCompany(@RequestBody Company company) {
  //    return companyRepository.save(company);
  //}

  // Update a Company
  //@PutMapping("/{id}")
  //public Company updateCompany(@PathVariable Integer id, @RequestBody Company companyDetails) {
  //    Company company = companyRepository.findById(id)
  //            .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Company not found"));
  //
  //    company.setName(companyDetails.getName());
  //    company.setDuration(companyDetails.getDuration());
  //    company.setProfile(companyDetails.getProfile());
  //    company.setStipend(companyDetails.getStipend());
  //    company.setWorkFromHome(companyDetails.getWorkFromHome());

  //    return companyRepository.save(company);
  //}

  // Delete a Company
  //@DeleteMapping("/{id}")
  //@ResponseStatus(HttpStatus.NO_CONTENT)
  //public void deleteCompany(@PathVariable Integer id) {
  //    if (!companyRepository.existsById(id)) {
  //        throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Company not found");
  //    }
  //    companyRepository.deleteById(id);
  //}
}