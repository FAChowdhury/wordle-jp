#pragma once
#include <array>
#include <cstdint>

#include "dictionary_constants.hpp"

namespace dictionary {
    struct RadicalRange {
        std::uint32_t offset;
        std::uint16_t count;
    };

    struct Entry {
        char32_t kanji;
        RadicalRange radicals;
    };

    inline constexpr std::array<Entry, KANJI_COUNT> entries {

    };
};
