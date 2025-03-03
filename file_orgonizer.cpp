#include <iostream>
#include <filesystem>
#include <fstream>
#include <map>
#include <vector>

namespace fs = std::filesystem;

// Function to load file categories from config file
std::map<std::string, std::string> loadCategories(const std::string& configFile) {
    std::map<std::string, std::string> fileCategories;
    std::ifstream file(configFile);

    if (!file) {
        std::cerr << "Error: Unable to open config file!" << std::endl;
        return fileCategories;
    }

    std::string extension, category;
    while (file >> extension >> category) {
        fileCategories[extension] = category;
    }

    file.close();
    return fileCategories;
}

// Function to organize files recursively
void organizeFiles(const std::string& directory, const std::map<std::string, std::string>& fileCategories) {
    for (const auto& entry : fs::recursive_directory_iterator(directory)) {
        if (fs::is_regular_file(entry)) {
            std::string extension = entry.path().extension().string();

            // Check if the extension exists in the map
            if (fileCategories.find(extension) != fileCategories.end()) {
                std::string folderName = fileCategories.at(extension);
                fs::path targetFolder = directory + "/" + folderName;

                // Create folder if it does not exist
                if (!fs::exists(targetFolder)) {
                    fs::create_directory(targetFolder);
                }

                // Move file to the categorized folder
                fs::path targetPath = targetFolder / entry.path().filename();
                fs::rename(entry.path(), targetPath);

                std::cout << "Moved: " << entry.path().filename() << " -> " << targetFolder << std::endl;
            }
        }
    }
}

int main() {
    std::string directory;
    std::cout << "Enter the directory path to organize: ";
    std::getline(std::cin, directory);

    if (!fs::exists(directory) || !fs::is_directory(directory)) {
        std::cerr << "Invalid directory!" << std::endl;
        return 1;
    }

    // Load file categories from config file
    std::map<std::string, std::string> fileCategories = loadCategories("config.txt");
    if (fileCategories.empty()) {
        std::cerr << "No categories loaded. Exiting..." << std::endl;
        return 1;
    }

    organizeFiles(directory, fileCategories);
    std::cout << "File organization completed!" << std::endl;

    return 0;
}