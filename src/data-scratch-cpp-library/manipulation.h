
#include "gradient_descent.h"
#include "linear_algebra.h"
#include "stats.h"

double parse_row(input_row, parsers) ;
double parse_rows_with(reader, parsers);
double try_or_none(arbitrary_function);
double try_parse_field(field_name, value, parser_dict);
double parse_dict(input_dict, parser_dict);
double picker(field_name);
double pluck(field_name, rows);
double group_by(grouper, rows, value_transform=None);
double scale(std::vector<std::vector<double>> data_matrix);
double rescale(std::vector<std::vector<double>> data_matrix);
std::vector<std::vector<double>> de_mean_matrix(std::vector<std::vector<double>> a_matrix);
std::vector<double> direction(std::vector<double> w);
double directional_variance_i(double x_i, std::vector<double> w);
double directional_variance(std::vector<std::vector<double>> x_matrix, std::vector<double>w);
double directional_variance_gradient_i(double x_i, std::vector<double>w);
double directional_variance_gradient(std::vector<std::vector<double>> x_matrix, std::vector<double>w);
double first_principal_component(std::vector<std::vector<double>> x_matrix);
double first_principal_component_sgd(std::vector<std::vector<double>> matrix_x);
double project(std::vector<double> v, std::vector<double>w);
double remove_projection_from_vector(std::vector<double> v, std::vector<double>w);
double remove_projection(std::vector<std::vector<double>> x_matrix, std::vector<double>w);
double principal_component_analysis(std::vector<double> x_vector, double num_components);
std::vector<double> transform_vector(std::vector<double> v, std::vector<std::vector<double>> components);
double transform(std::vector<double> x_vector, std::vector<std::vector<double>> components);