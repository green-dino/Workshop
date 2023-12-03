// Naming Conventions and Considerations for Microcontroller/Processor

// Constants
// Rule: UPPERCASE_WITH_UNDERSCORE_SEPARATION
// Example: HIGH_TEMPERATURE
#define HIGH_TEMPERATURE

// Local Variable Name
// Rule: lowercaseWithBumpyCaps (underscores optional)
// Example: currentTemperature
int currentTemperature;

// Global Variable Name
// Rule: glLowercaseWithBumpyCaps (underscores optional)
// Note: Globals should be contained to a single module
// Example: gl_maximumRecordedTemperature
int gl_maximumRecordedTemperature;

// Function Names
// Rule: UPPERCASE_WITH_BUMPY_CAPS (underscores optional) with active voice
// Example: ConvertFarenheitToCentigrade(...)
void ConvertFarenheitToCentigrade(...);

// Object Names
// Rule: obLowercaseWithBumpyCaps
// Example: ob_myTempRecorder
struct ob_myTempRecorder {
    // members...
};

// Module
// Rule: An underscore followed by lowercaseWithBumpyCaps
// Example: _tempRecorder
#include "_tempRecorder.h"

// Class Names
// Rule: class_BumpyCaps (keep brief)
// Example: class_TempSystem
class TempSystem {
    // members and methods...
};
