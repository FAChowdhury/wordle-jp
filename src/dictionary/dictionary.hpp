# pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <span>

#include "dictionary_entries.hpp"
#include "dictionary_radicals.hpp"

namespace dictionary {
	class Dictionary final {
	public:
		Dictionary() = delete;

		[[nodiscard]]
		static constexpr bool Contains(char32_t kanji);

		[[nodiscard]]
		static constexpr std::span<const char32_t> GetRadicals(char32_t kanji);

	private:
		static constexpr auto& entries = dictionary::entries;
		static constexpr auto& radicals = dictionary::radicals;
	};
};
