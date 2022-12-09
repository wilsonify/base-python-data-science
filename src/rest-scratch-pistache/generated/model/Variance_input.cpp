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


#include "Variance_input.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Variance_input::Variance_input()
{
    m_xIsSet = false;
    
}

void Variance_input::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Variance_input::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Variance_input::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Variance_input" : pathPrefix;

         
    if (XIsSet())
    {
        const std::vector<double>& value = m_x;
        const std::string currentValuePath = _pathPrefix + ".X";
                
        
        { // Recursive validation of array elements
            const std::string oldValuePath = currentValuePath;
            int i = 0;
            for (const double& value : value)
            { 
                const std::string currentValuePath = oldValuePath + "[" + std::to_string(i) + "]";
                        
        
 
                i++;
            }
        }

    }
    
    return success;
}

bool Variance_input::operator==(const Variance_input& rhs) const
{
    return
    
    
    
    ((!XIsSet() && !rhs.XIsSet()) || (XIsSet() && rhs.XIsSet() && getX() == rhs.getX()))
    
    ;
}

bool Variance_input::operator!=(const Variance_input& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Variance_input& o)
{
    j = nlohmann::json();
    if(o.XIsSet() || !o.m_x.empty())
        j["x"] = o.m_x;
    
}

void from_json(const nlohmann::json& j, Variance_input& o)
{
    if(j.find("x") != j.end())
    {
        j.at("x").get_to(o.m_x);
        o.m_xIsSet = true;
    } 
    
}

std::vector<double> Variance_input::getX() const
{
    return m_x;
}
void Variance_input::setX(std::vector<double> const value)
{
    m_x = value;
    m_xIsSet = true;
}
bool Variance_input::XIsSet() const
{
    return m_xIsSet;
}
void Variance_input::unsetx()
{
    m_xIsSet = false;
}


} // namespace org::openapitools::server::model

