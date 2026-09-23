"use client";
import React from "react";
import { useState, useEffect } from "react"
import { ApexOptions } from "apexcharts";
import dynamic from "next/dynamic";

const ReactApexChart = dynamic(() => import("react-apexcharts"),{
ssr:false,
});

export default function fxrates() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [time, setTime] = useState(new Date());

    function fetchData(){
        fetch('/api/fxrates/')
          .then((response) => response.json())
          .then((data) => {
            setData(data);
            setLoading(false);
            setTime(new Date());
          });
    }

    useEffect(() => {
      fetchData();
      const interval = setInterval(()=>{
        fetchData()
        },10000); // hard code the interval, no file generalconfig
        return () => clearInterval(interval);
    },[]);

    const height: string[] = [];
    const title: string[] = [];
    const descriptions: string[]=[];
    const colorsdef: string[] = [];
    const asat: string[]=[];
    const categoryarray: string[] = [];
    const series:{name:string,data:number[]}[]=[];

    for (const val of data){
      const k:string = val["key"];
      const v:string = val["value"]

      if (k == "#seriesName"){
        const rV = v.split(",");
        for (const r of rV){
          categoryarray.push(r);
        }
      }else{
        if (k=='#title') {
          title.push(v);
        }else{
        if (k=='#descriptions'){
          descriptions.push(v);
        }else{
          if (k=='#colors'){
            const clr = v.split(",");
            for (const cc of clr){
              colorsdef.push(cc);
            }
          }else{
            if(k=="#height"){
              height.push(v);
            }else{
              if(k=="#asat")
                asat.push(v);
              else{
              const rS = v.split(",");
              const r:number[]=[]
              for (const i of rS){
                r.push(Number(i));
                }
              series.push({name:k,data:r})
              }
              }

            }
          }
        }
      }
    }


    const options: ApexOptions = {
      legend:{
        show: true, // Hide legend
        position: "top",
        horizontalAlign: "left",
      },
      colors:colorsdef,
      chart:{
        fontFamily: "Outfit, sans-serif",
        height: 180,
        type: "line", // Set the chart type to 'line'
        toolbar: {
          show: false, // Hide chart toolbar
        },
      },
      annotations:{
        xaxis:[
          {
            x: categoryarray[categoryarray.length-14],
            borderColor: '#ffffff',
            label: {
              borderColor: '#000000',
              style: {
                color: '#000',
                background: '#ffffff',
              },
            offsetY: -40,
            text: 'Today',
            }
          },
          {
            x: categoryarray[categoryarray.length-14],
            x2: categoryarray[categoryarray.length-1],
            fillColor: '#e88e34',
            opacity: 0.4,
            label: {
              borderColor: '#965b20',
              style: {
                fontSize: '10px',
                color: '#fff',
                background: '#ef8114',
              },
              offsetY: 40,
              text: '14 Days Forecast',
            }
          }
        ]
      },
      stroke:{
        curve: "straight", // Define the line style (straight, smooth, or step)
        width: [2, 2], // Line width for each dataset
      },
      fill:{
        type: "gradient",
        gradient: {
          opacityFrom: 0.55,
          opacityTo: 0,
          },
        },
      markers:{
        size: 3, // Size of the marker points
        strokeColors: "#222", // Marker border color
        strokeWidth: 2,
        hover: {
          size: 6, // Marker size on hover
          },
        },
      grid:{
        xaxis:{
          lines: {
            show: false, // Hide grid lines on x-axis
          },
        },
        yaxis:{
          lines: {
            show: true, // Show grid lines on y-axis
          },
        }
      },
      forecastDataPoints: {
        count: 13
      }
      ,
      dataLabels:{
        enabled: false, // Disable data labels
      },
      tooltip:{
        enabled: true, // Enable tooltip
        x: {
          format: "dd MMM yyyy", // Format for x-axis tooltip
        },
      },
      xaxis:{
        type:"category",
        categories: categoryarray
      },
      yaxis:{
        labels:{
          style: {
          fontSize: "12px", // Adjust font size for y-axis labels
          colors: ["#6B7280"], // Color of the labels
          },
        },
        title:{
          text: "", // Remove y-axis title
          style: {
            fontSize: "12px",
          },
        }
      }
    };

    return(
      <div className="overflow-hidden rounded-2xl border border-gray-200 bg-white px-5 pt-5 dark:border-gray-800 dark:bg-white/[0.03] sm:px-6 sm:pt-6">
        <div className="flex items-center justify-between">
          <div className="w-full">
            <h3 className="text-lg font-semibold text-gray-800 dark:text-white/90">
              <span title = "AUD to foreign exchanged rates">
                {title[0]}
              </span>
              <span className="text-xs font-thin text-gray-800 dark:text-white/90">
                {asat[0]}
              </span>
            </h3>
            <p className="mt-1 text-gray-500 text-theme-sm dark:text-grey-400">
              {descriptions[0]}
            </p>
          </div>
        </div>

        <div className = "max-w-full overflow-x-auto custom-scrollbar">
          <div className="min-w-[1000px] xl:min-w-full">
            <ReactApexChart
              options={options}
              series={series}
              type="area" //line
              height={310}
              />
          </div>
        </div>
      </div>
    );
}