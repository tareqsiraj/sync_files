#include "config.hpp"

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wshadow-field"
#include <boost/program_options.hpp>
#pragma clang diagnostic pop

#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h>

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

  auto console = spdlog::stdout_color_mt(sync_files::CONSOLE_LOGGER);
  console->info("foobar");

  return 0;
}
