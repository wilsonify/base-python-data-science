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


#include "Partial_difference_quotient_input.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Partial_difference_quotient_input::Partial_difference_quotient_input()
{
    m_vIsSet = false;
    m_iIsSet = false;
    m_hIsSet = false;
    
}

void Partial_difference_quotient_input::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Partial_difference_quotient_input::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Partial_difference_quotient_input::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Partial_difference_quotient_input" : pathPrefix;

         
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
            
    return success;
}

bool Partial_difference_quotient_input::operator==(const Partial_difference_quotient_input& rhs) const
{
    return
    
    
    
    ((!VIsSet() && !rhs.VIsSet()) || (VIsSet() && rhs.VIsSet() && getV() == rhs.getV())) &&
    
    
    ((!IIsSet() && !rhs.IIsSet()) || (IIsSet() && rhs.IIsSet() && getI() == rhs.getI())) &&
    
    
    ((!HIsSet() && !rhs.HIsSet()) || (HIsSet() && rhs.HIsSet() && getH() == rhs.getH()))
    
    ;
}

bool Partial_difference_quotient_input::operator!=(const Partial_difference_quotient_input& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Partial_difference_quotient_input& o)
{
    j = nlohmann::json();
    if(o.VIsSet() || !o.m_v.empty())
        j["v"] = o.m_v;
    if(o.IIsSet())
        j["i"] = o.m_i;
    if(o.HIsSet())
        j["h"] = o.m_h;
    
}

void from_json(const nlohmann::json& j, Partial_difference_quotient_input& o)
{
    if(j.find("v") != j.end())
    {
        j.at("v").get_to(o.m_v);
        o.m_vIsSet = true;
    } 
    if(j.find("i") != j.end())
    {
        j.at("i").get_to(o.m_i);
        o.m_iIsSet = true;
    } 
    if(j.find("h") != j.end())
    {
        j.at("h").get_to(o.m_h);
        o.m_hIsSet = true;
    } 
    
}

std::vector<double> Partial_difference_quotient_input::getV() const
{
    return m_v;
}
void Partial_difference_quotient_input::setV(std::vector<double> const value)
{
    m_v = value;
    m_vIsSet = true;
}
bool Partial_difference_quotient_input::VIsSet() const
{
    return m_vIsSet;
}
void Partial_difference_quotient_input::unsetv()
{
    m_vIsSet = false;
}
org::openapitools::server::model::Object Partial_difference_quotient_input::getI() const
{
    return m_i;
}
void Partial_difference_quotient_input::setI(org::openapitools::server::model::Object const& value)
{
    m_i = value;
    m_iIsSet = true;
}
bool Partial_difference_quotient_input::IIsSet() const
{
    return m_iIsSet;
}
void Partial_difference_quotient_input::unseti()
{
    m_iIsSet = false;
}
org::openapitools::server::model::Object Partial_difference_quotient_input::getH() const
{
    return m_h;
}
void Partial_difference_quotient_input::setH(org::openapitools::server::model::Object const& value)
{
    m_h = value;
    m_hIsSet = true;
}
bool Partial_difference_quotient_input::HIsSet() const
{
    return m_hIsSet;
}
void Partial_difference_quotient_input::unseth()
{
    m_hIsSet = false;
}


} // namespace org::openapitools::server::model

