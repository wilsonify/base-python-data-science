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


#include "Train_test_split_input.h"
#include "Helpers.h"

#include <sstream>

namespace org::openapitools::server::model
{

Train_test_split_input::Train_test_split_input()
{
    m_xIsSet = false;
    m_yIsSet = false;
    m_p = 0.0;
    m_pIsSet = false;
    
}

void Train_test_split_input::validate() const
{
    std::stringstream msg;
    if (!validate(msg))
    {
        throw org::openapitools::server::helpers::ValidationException(msg.str());
    }
}

bool Train_test_split_input::validate(std::stringstream& msg) const
{
    return validate(msg, "");
}

bool Train_test_split_input::validate(std::stringstream& msg, const std::string& pathPrefix) const
{
    bool success = true;
    const std::string _pathPrefix = pathPrefix.empty() ? "Train_test_split_input" : pathPrefix;

         
    if (XIsSet())
    {
        const std::vector<std::vector<double>>& value = m_x;
        const std::string currentValuePath = _pathPrefix + ".X";
                
        
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
         
    if (YIsSet())
    {
        const std::vector<std::vector<double>>& value = m_y;
        const std::string currentValuePath = _pathPrefix + ".Y";
                
        
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

bool Train_test_split_input::operator==(const Train_test_split_input& rhs) const
{
    return
    
    
    
    ((!XIsSet() && !rhs.XIsSet()) || (XIsSet() && rhs.XIsSet() && getX() == rhs.getX())) &&
    
    
    ((!YIsSet() && !rhs.YIsSet()) || (YIsSet() && rhs.YIsSet() && getY() == rhs.getY())) &&
    
    
    ((!PIsSet() && !rhs.PIsSet()) || (PIsSet() && rhs.PIsSet() && getP() == rhs.getP()))
    
    ;
}

bool Train_test_split_input::operator!=(const Train_test_split_input& rhs) const
{
    return !(*this == rhs);
}

void to_json(nlohmann::json& j, const Train_test_split_input& o)
{
    j = nlohmann::json();
    if(o.XIsSet() || !o.m_x.empty())
        j["x"] = o.m_x;
    if(o.YIsSet() || !o.m_y.empty())
        j["y"] = o.m_y;
    if(o.PIsSet())
        j["p"] = o.m_p;
    
}

void from_json(const nlohmann::json& j, Train_test_split_input& o)
{
    if(j.find("x") != j.end())
    {
        j.at("x").get_to(o.m_x);
        o.m_xIsSet = true;
    } 
    if(j.find("y") != j.end())
    {
        j.at("y").get_to(o.m_y);
        o.m_yIsSet = true;
    } 
    if(j.find("p") != j.end())
    {
        j.at("p").get_to(o.m_p);
        o.m_pIsSet = true;
    } 
    
}

std::vector<std::vector<double>> Train_test_split_input::getX() const
{
    return m_x;
}
void Train_test_split_input::setX(std::vector<std::vector<double>> const& value)
{
    m_x = value;
    m_xIsSet = true;
}
bool Train_test_split_input::XIsSet() const
{
    return m_xIsSet;
}
void Train_test_split_input::unsetx()
{
    m_xIsSet = false;
}
std::vector<std::vector<double>> Train_test_split_input::getY() const
{
    return m_y;
}
void Train_test_split_input::setY(std::vector<std::vector<double>> const& value)
{
    m_y = value;
    m_yIsSet = true;
}
bool Train_test_split_input::YIsSet() const
{
    return m_yIsSet;
}
void Train_test_split_input::unsety()
{
    m_yIsSet = false;
}
double Train_test_split_input::getP() const
{
    return m_p;
}
void Train_test_split_input::setP(double const value)
{
    m_p = value;
    m_pIsSet = true;
}
bool Train_test_split_input::PIsSet() const
{
    return m_pIsSet;
}
void Train_test_split_input::unsetp()
{
    m_pIsSet = false;
}


} // namespace org::openapitools::server::model

