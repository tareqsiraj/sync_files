#include <boost/program_options.hpp>

#include <iostream>

int main(int argc, const char* argv[]) {
  boost::program_options::options_description desc{"Allowed options"};

  // clang-format off
    desc.add_options()
        ("help", "Show this help message.")
    ;
  // clang-format on

  boost::program_options::variables_map vm{};
  boost::program_options::store(boost::program_options::parse_command_line(argc, argv, desc), vm);
  boost::program_options::notify(vm);

  if (vm.count("help")) {
    std::cout << desc << "\n";
    return 0;
  }

  return 0;
}
