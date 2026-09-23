"use client";
import dynamic from "next/dynamic";
import React from "react";
import { useEffect, useState } from "react";
import { ApexOptions } from "apexcharts";
import { useTheme }from "../../../context/ThemeContext";
const generalConfig = require('');
import prisma from 'prisma';
import ChartTab from "../../common/ChartTab";
import { HorizontaLDots } from "@/icons";

// Dynamically import the ReactApexChart component
const ReactApexChart = dynamic(() => import("react-apexcharts"), {
  ssr: false,
});

//set up function to retrieve data
type PropsType = {
	queryName: string;
}

export default function callkpi( { queryName }: PropsType) {
	const theme = useTheme(); // import { useTheme } from "../../context/ThemeContext";
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);

	function fetchData() {
		fetch('api'+queryName)
			.then((response)=> response.json())
			.then((data) => {
				setData(data);
				setLoading(false);
			});
	}
    //function call to retrieve data
    
    useEffect(() => {
	fetchData();
	const interval = setInterval(() => {
		fetchData()
	}, generalConfig.refresh);
	return () => clearInterval(interval);
    }, []);

    if (loading || !data || data.length == 0){
        return(
            <div>

            </div>
        )
    }
    const seriesDummy = [{name: 'Dummy', data: [1,2,3],}];

    var itemCategories = [""];
    var seriesData = [];

    for (const val of data) {

    }

    const options: ApexOptions = {
        chart: {
            type: "area",
            height: 210
        },
        legend: {
            show: true,
            position: "top",
            horizontalAlign: "left",
        },

        xaxis: {
	    categories: itemCategories
        }

    }

//array list to store data
// options = {options}
// series = {seriesData && seriesData.length > 0 ? seriesData : seriesDummy}
    return (
        <div>
            <ReactApexChart
          options={options}
          //series = {seriesData && seriesData.length > 0 ? seriesData : seriesDummy}
          type="area"
          height={310}
            />
        </div>
    );
}





