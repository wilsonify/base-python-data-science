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


#include "Vector_sum_input.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Vector_sum_input::Vector_sum_input()
{
    m_vIsSet = false;
    m_wIsSet = false;
    
}

void Vector_sum_input::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Vector_sum_input::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Vector_sum_input::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Vector_sum_input" : pathPrefix;

         
    if (VIsSet())
    {
        const std::vector<double>& value = m_v;
        const std::string currentValuePath = _pathPrefix + ".V";
                
        
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
         
    if (WIsSet())
    {
        const std::vector<double>& value = m_w;
        const std::string currentValuePath = _pathPrefix + ".W";
                
        
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

bool Vector_sum_input::operator==(const Vector_sum_input& rhs) const
{
    return
    
    
    
    ((!VIsSet() && !rhs.VIsSet()) || (VIsSet() && rhs.VIsSet() && getV() == rhs.getV())) &&
    
    
    ((!WIsSet() && !rhs.WIsSet()) || (WIsSet() && rhs.WIsSet() && getW() == rhs.getW()))
    
    ;
}

bool Vector_sum_input::operator!=(const Vector_sum_input& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Vector_sum_input& o)
{
    j = nlohmann::json();
    if(o.VIsSet() || !o.m_v.empty())
        j["v"] = o.m_v;
    if(o.WIsSet() || !o.m_w.empty())
        j["w"] = o.m_w;
    
}

void from_json(const nlohmann::json& j, Vector_sum_input& o)
{
    if(j.find("v") != j.end())
    {
        j.at("v").get_to(o.m_v);
        o.m_vIsSet = true;
    } 
    if(j.find("w") != j.end())
    {
        j.at("w").get_to(o.m_w);
        o.m_wIsSet = true;
    } 
    
}

std::vector<double> Vector_sum_input::getV() const
{
    return m_v;
}
void Vector_sum_input::setV(std::vector<double> const value)
{
    m_v = value;
    m_vIsSet = true;
}
bool Vector_sum_input::VIsSet() const
{
    return m_vIsSet;
}
void Vector_sum_input::unsetv()
{
    m_vIsSet = false;
}
std::vector<double> Vector_sum_input::getW() const
{
    return m_w;
}
void Vector_sum_input::setW(std::vector<double> const value)
{
    m_w = value;
    m_wIsSet = true;
}
bool Vector_sum_input::WIsSet() const
{
    return m_wIsSet;
}
void Vector_sum_input::unsetw()
{
    m_wIsSet = false;
}


} // namespace org::openapitools::server::model

