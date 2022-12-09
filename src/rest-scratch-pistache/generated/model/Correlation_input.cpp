/**
* Minimal Pistache
* This is a sample server
*
* The version of the OpenAPI document: 1.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/


#include "Correlation_input.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Correlation_input::Correlation_input()
{
    m_DataIsSet = false;
    
}

void Correlation_input::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Correlation_input::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Correlation_input::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Correlation_input" : pathPrefix;

         
    if (dataIsSet())
    {
        const std::vector<std::vector<double>>& value = m_Data;
        const std::string currentValuePath = _pathPrefix + ".data";
                
        
        { // Recursive validation of array elements
            const std::string oldValuePath = currentValuePath;
            int i = 0;
            for (const std::vector<double>& value : value)
            { 
                const std::string currentValuePath = oldValuePath + "[" + std::to_string(i) + "]";
                        
        
        { // Recursive validation of array elements
            const std::string oldValuePath = currentValuePath;
            int i = 0;
            for (const double& value : value)
            { 
                const std::string currentValuePath = oldValuePath + "[" + std::to_string(i) + "]";
                        
        
 
                i++;
            }
        }
 
                i++;
            }
        }

    }
    
    return success;
}

bool Correlation_input::operator==(const Correlation_input& rhs) const
{
    return
    
    
    
    ((!dataIsSet() && !rhs.dataIsSet()) || (dataIsSet() && rhs.dataIsSet() && getData() == rhs.getData()))
    
    ;
}

bool Correlation_input::operator!=(const Correlation_input& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Correlation_input& o)
{
    j = nlohmann::json();
    if(o.dataIsSet() || !o.m_Data.empty())
        j["data"] = o.m_Data;
    
}

void from_json(const nlohmann::json& j, Correlation_input& o)
{
    if(j.find("data") != j.end())
    {
        j.at("data").get_to(o.m_Data);
        o.m_DataIsSet = true;
    } 
    
}

std::vector<std::vector<double>> Correlation_input::getData() const
{
    return m_Data;
}
void Correlation_input::setData(std::vector<std::vector<double>> const& value)
{
    m_Data = value;
    m_DataIsSet = true;
}
bool Correlation_input::dataIsSet() const
{
    return m_DataIsSet;
}
void Correlation_input::unsetData()
{
    m_DataIsSet = false;
}


} // namespace org::openapitools::server::model

