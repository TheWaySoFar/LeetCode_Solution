#!/bin/bash

awk '{
    if($0 ~ /^[0-9]+ - .*$/){
        str=""
        while(1){
            if($0 ~ /^[0-9]+ - .*$/){
                if(str!=""){
                    if(index(str, "High")!=0){
                        print str
                    }
                } 
                str=$0 
            } else if($0 ~ /^$/){
                break
            } else {
                str=str"\n"$0
            }
            getline
        }
    }
}' 